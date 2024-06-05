import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import random

def get_file_path():
    path = r'C:\Users\Axioo Pongo\Documents\capstone project\data_mentah\user_information.csv'
    return path

def get_dataframe(path):
    df = pd.read_csv(path, sep=',')
    return df

def generate_random_data(size):
    
    first_names = [
        'John', 'Jane', 'Alex', 'Emily', 'Chris', 'Katie', 'Michael', 'Sarah',
        'David', 'Laura', 'James', 'Linda', 'Robert', 'Patricia', 'Charles', 'Barbara',
        'Joseph', 'Susan', 'Thomas', 'Jessica', 'Brian', 'Karen', 'Daniel', 'Nancy',
        'Kevin', 'Lisa', 'Paul', 'Margaret', 'Mark', 'Betty'
    ]
    last_names = [
        'Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson',
        'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin',
        'Thompson', 'Garcia', 'Martinez', 'Robinson', 'Clark', 'Rodriguez', 'Lewis',
        'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'King'
    ]
    names = [random.choice(first_names) + ' ' + random.choice(last_names) for _ in range(size)]
    

    ages = np.random.randint(18, 71, size)
    
    countries = [
        'USA', 'Canada', 'UK', 'Germany', 'France', 'Australia', 'India', 'China', 'Brazil', 
        'South Africa', 'Mexico', 'Italy', 'Spain', 'Russia', 'Japan', 'South Korea',
        'Netherlands', 'Turkey', 'Saudi Arabia', 'Argentina', 'Sweden', 'Norway', 'Denmark', 
        'Finland', 'Belgium', 'Switzerland', 'Poland', 'Austria', 'New Zealand', 'Ireland'
    ]
    country = [random.choice(countries) for _ in range(size)]
    
    genders = ['Male', 'Female', 'Other']
    gender = [random.choice(genders) for _ in range(size)]
    
    return names, ages, country, gender

def add_column_header(df):
    df.columns = ['user_id']
    
    names, ages, countries, genders = generate_random_data(len(df))
    
    df['name'] = names
    df['age'] = ages
    df['country'] = countries
    df['gender'] = genders
    
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
    clean_data.to_sql(name='user_information', con=conn, if_exists='replace', schema='public', index=False)
    return clean_data

path = get_file_path()
df = get_dataframe(path)
clean_data = add_column_header(df)
conn = get_postgres_connection()
to_postgres = load_to_postgres(conn, clean_data)
print(to_postgres)
