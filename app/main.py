import database_connect

def main():
    
    dbcred = {
        "user": "postgres",
        "password": "postgres",
        "host": "127.0.0.1",
        "port": "5432",
        "database": "fastapi",
        "cursor_factory": RealDictCursor
    }

    cursor = get_database_cursor(dbcred)

    cursor.close()
    cursor.connection.close()

if __name__ == '__main__':
    main()