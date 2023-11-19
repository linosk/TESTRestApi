import unittest
from unittest.mock import patch, mock_open
from app.database_connect import get_credentials
from app.database_connect import get_database_cursor


class TestDatabaseConnect(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='{"user": "user","password": "password","host": "host","port": "port","database": "database"}')
    def test_get_credentials_correct_format(self, mock_open, mock_json_load):

        assert get_credentials("path") == False

if __name__ == '__main__':
    unittest.main()