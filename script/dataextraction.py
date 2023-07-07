import psycopg2
import dotenv
import os
import sqlparse
import pandas as pd

# Loads the environment variables from the .env file
dotenv.load_dotenv()

# Formats the given SQL query
def format_sql(sql):
    """
        Description: Formats the given SQL query
        sql: SQL query to format
    """
    parsed = sqlparse.parse(sql)
    formatted = sqlparse.format(str(parsed[0]), reindent=True, keyword_case='upper')
    return formatted

# Connects to the database and returns the connection object
def connect_to_database():
    """
        Description: Connects to the database and returns the connection object
    """
    dbname = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")

    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        print("Connected to the PostgreSQL database")
        return conn

    except psycopg2.Error as e:
        print("Error connecting to the PostgreSQL database:", e)
        return None

# Returns a string of all unique columns across the given table names
def get_unique_columns(cursor, table_names):
    """
        Description: Returns a string of all unique columns across the given table names
        cursor: psycopg2 cursor object
        table_names: list of table names to join
    """
    unique_table_column = {}
    for table_name in table_names:
        cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'")
        columns = [column[0] for column in cursor.fetchall()]
        for column in columns:
            unique_table_column[column] = table_name
    result = ', '.join(f"{value}.{key}" for key, value in unique_table_column.items())
    return result

# Creates view from the given table names and selected columns
def create_view(cursor, selected_columns, table_names, view_name, foreign_key):
    """
        Description: Creates view from the given table names and selected columns
        cursot: psycopg2 cursor object
        selected_columns: string of columns to select, these columns must be unique across all tables
        table_names: list of table names to join
        view_name: name of the view to create
        foreign_key: name of the foreign key to join on
    """
    join_conditions = [f"{table}.{foreign_key} = {table_names[0]}.{foreign_key}" for table in table_names[1:]]
    join_clause = "\n".join(f"JOIN {table} ON {join_condition}" for table, join_condition in zip(table_names[1:], join_conditions))
    
    view_clause = (f"""CREATE VIEW {view_name} AS 
                      SELECT {selected_columns} 
                      FROM {table_names[0]}
                      {join_clause}""")
    print(f"Created view {view_clause}")

# Creates the base dataset
def create_dataset(cursor, table_names):
    """
        Description: Creates the base dataset
        cursor: psycopg2 cursor object
        table_names: list of table names to join, not that they should be based on refined schema
    """
    selected_columns = get_unique_columns(cursor, table_names)
    create_view(cursor, selected_columns, table_names, view_name="refined.base_dataset", foreign_key="icustay_id")

def get_base_dataset(cursor):
    """
        Description: Returns the base dataset
        cursor: psycopg2 cursor object
    """
    cursor.execute("SELECT * FROM refined.base_dataset")
    return cursor.fetchall()


conn = connect_to_database()
cur = conn.cursor()

first_day_tables = [
    "gcs_first_day",
    "height_first_day",
    "urine_output_first_day",
    "ventilation_first_day",
    "vitals_first_day",
    "weight_first_day",
    "labs_first_day",
    "rrt_first_day",
]

base_tables = [
    "patients",
    "first_day"
]

create_dataset(cur, base_tables)

# selected_columns = get_unique_columns(cur, table_name=first_day_table_names)
# create_view(cur, selected_columns, first_day_table_names, view_name="refined.first_day", foreign_key="icustay_id")    