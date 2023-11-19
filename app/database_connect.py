import json
import psycopg2
from psycopg2.extensions import cursor
from psycopg2 import Error
from psycopg2.extras import RealDictCursor

def get_credentials(path) -> dict:
    
    with open(path, 'r') as file:
        credentials = json.load(file)

    return credentials


def get_database_cursor(credentials) -> cursor:
    
    try:
        connection = psycopg2.connect(
            user=credentials["user"],
            password=credentials["password"],
            host=credentials["host"],
            port=credentials["port"],
            database=credentials["database"],
            #This makes it so that returned psql entries are dictonaries instead of tuples
            cursor_factory=RealDictCursor
        )

        cursor = connection.cursor()
        print("Database connection was succesfull.")

        return cursor

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if connection is not None:
            cursor.close()
            connection.close()
            print("Database connection closed.")