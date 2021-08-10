from sqlalchemy import create_engine
import pandas as pd
from app.insert_into_mongo import df_to_mongo
from app.save_locally import write_df_as_json
from app.constants import table_idx

def postgres_to_json():
    engine = create_engine('postgresql://northwind_user:thewindisblowing@localhost:5432/northwind')
    
    for table_name in table_idx.keys():
        if table_name != 'order_details':
            df = pd.read_sql_query(f'select * from "{table_name}"', con=engine)
            if not df.empty:
                write_df_as_json(df, 'postgres', table_name)
                df_to_mongo(df, table_name)

