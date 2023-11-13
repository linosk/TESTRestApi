import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(
        user="postgres",
        password="postgres",
        host="127.0.0.1",
        port="5432",
        database="fastapi"
    )

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)