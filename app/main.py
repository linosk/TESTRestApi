import database_connect
from psycopg2.extras import RealDictCursor

def main():
    credentials = database_connect.get_credentials("credentials")
    cursor = database_connect.get_database_cursor(credentials)

if __name__ == '__main__':
    main()