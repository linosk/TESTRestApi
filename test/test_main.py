import unittest
from psycopg2 import Error, OperationalError
from psycopg2.extras import RealDictCursor
import app.main

#find out the naming convention
#think about better structuring
#is this good practice?
class TestMain(unittest.TestCase):

    @unittest.expectedFailure
    def test_get_database_cursor(self):

        dbcred = {
            "user": "postgres",
            "password": "wrong_password",
            "host": "127.0.0.1",
            "port": "5432",
            "database": "fastapi",
            "cursor_factory": RealDictCursor
        }

        with self.assertRaises(OperationalError):
            cursor = app.main.get_database_cursor(dbcred)

