from datetime import datetime
from pathlib import Path

def write_df_as_json(df, source, table_name):
    today = datetime.today().strftime('%Y-%m-%d')

    filepath = f'local_data/{source}/{today}'
    Path(filepath).mkdir(parents=True, exist_ok=True)

    filename = f'{table_name}.json'

    df.to_json(f'{filepath}/{filename}')
