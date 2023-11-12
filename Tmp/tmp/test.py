import unittest
import app

#export PYTHONPATH=/home/me/Projects/:$PYTHONPATH

class TestMain(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(0,4),4)
        self.assertEqual(calc.add(-4,8),4)
        self.assertEqual(calc.add(2,2),4)

#?
if __name__ == '__main__':
    unittest.main()