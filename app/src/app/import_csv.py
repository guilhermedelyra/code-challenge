import pandas as pd
from app.insert_into_mongo import df_to_mongo
from app.save_locally import write_df_as_json

def csv_to_json(csv_path):
    df = pd.read_csv(csv_path, header=0)
    table_name = 'order_details'
    write_df_as_json(df, 'csv', table_name)
    df_to_mongo(df, table_name)

def call_import():
    csv_to_json('./db_specification/order_details.csv')
