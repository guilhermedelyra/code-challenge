from pymongo import MongoClient

def search(table_name, id_field, id, db_url='localhost', db_port=27017):
    client = MongoClient(db_url, db_port)
    db = client['northwind']
    table = db[table_name]

    return [doc for doc in table.find({id_field: id})]

def example_queries():
    print(search('products', 'product_id', 20))
    print(search('orders', 'order_id', 10248))
