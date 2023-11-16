import psycopg2
from psycopg2 import Error
from psycopg2.extras import RealDictCursor

def get_database_cursor(credentials):
    
    try:
        connection = psycopg2.connect(
            user=credentials["user"],
            password=credentials["password"],
            host=credentials["host"],
            port=credentials["port"],
            database=credentials["database"],
            cursor_factory=credentials["cursor_factory"]
        )

        cursor = connection.cursor()
        print("Database connection was succesfull.")

        #cursor.execute("SELECT * FROM games;")
        #result = cursor.fetchall()
        #print(result)

        return cursor

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if connection is not None:
            connection.close()
            print("Database connection closed.")