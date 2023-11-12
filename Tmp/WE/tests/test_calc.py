import unittest
from source.calc import add

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1,3),4)
        #self.assertEqual(add(1,3),5)

if __name__ == '__main__':
    unittest.main()