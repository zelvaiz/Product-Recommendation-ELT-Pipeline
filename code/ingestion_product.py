import pandas as pd
from sqlalchemy import create_engine

def get_file_path():
    path = r'C:\Users\Axioo Pongo\Documents\capstone project\data_mentah\product information.csv' 
    return path

def get_dataframe(path):
    df = pd.read_csv(path, sep=',')
    return df

def get_postgres_connection():
    user = "postgres"
    host = "localhost"
    database = "capstone"
    port = 5432
    conn_string = f"postgresql://{user}@{host}:{port}/{database}"
    engine = create_engine(conn_string)
    
    return engine

def load_to_postgres(conn, clean_data):
    clean_data.to_sql(name='product', con=conn, if_exists='replace', schema='public')
    return clean_data

path = get_file_path()
df = get_dataframe(path)
conn = get_postgres_connection()
to_postgres = load_to_postgres(conn, df)
print(to_postgres)
