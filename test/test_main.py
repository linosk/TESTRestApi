import unittest
import app.main
import psycopg2
from psycopg2.extras import RealDictCursor

class TestMain(unittest.TestCase):

    def test_get_database_cursor(self):

        dbcred = {
            "user": "postgres",
            "password": "postgres",
            "host": "127.0.0.1",
            "port": "5432",
            "database": "fastapi",
            "cursor_factory": RealDictCursor
        }

        cursor = app.main.get_database_cursor(dbcred)

        self.assertIsInstance(cursor, psycopg2.extensions.cursor)

        cursor.close()
        cursor.connection.close()