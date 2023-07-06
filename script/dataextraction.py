import psycopg2
import dotenv
import os

# Load the environment variables from the .env file
dotenv.load_dotenv()

def connect_to_database():
    dbname = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")

    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        cursor = conn.cursor()
        return conn, cursor

    except psycopg2.Error as e:
        print("Error connecting to the PostgreSQL database:", e)
        return None, None

connect_to_database()