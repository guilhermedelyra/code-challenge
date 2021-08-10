from pymongo import MongoClient, ASCENDING, errors
import json
from app.constants import table_idx, table_relationships

def df_to_mongo(df, table_name, db_url='localhost', db_port=27017):
    payload = json.loads(df.to_json(orient='records'))
    client = MongoClient(db_url, db_port)
    db = client['northwind']
    table = db[table_name]

    primary_keys = table_idx[table_name]
    foreign_keys = table_relationships.get(table_name, [])

    indexes = [
        (col, ASCENDING) for 
        col in primary_keys
    ]
    table.create_index(indexes, unique=True)
    
    try:
        table.insert_many(payload)
        aggregate_child_tables(table, foreign_keys, table_name)
    except errors.BulkWriteError as err:
        check_for_error_if_not_duplicate_keys(err)

def aggregate_child_tables(table, foreign_keys, table_name):
    print(table_name)
    pipeline = []
    for child in foreign_keys:
        idx = table_idx[child][0]
        pipeline.append({
                '$lookup': {
                    'from': child,
                    'localField': idx,
                    'foreignField': idx,
                    'as': child
                },
        })

    cur = table.aggregate(pipeline)
    for doc in cur:
        print(doc)
        table.replace_one({'_id': doc['_id']}, doc)


def check_for_error_if_not_duplicate_keys(err):
    panic = filter(lambda x: x['code'] != 11000, err.details['writeErrors'])

    if len(panic) > 0:
        raise errors.BulkWriteError(panic)