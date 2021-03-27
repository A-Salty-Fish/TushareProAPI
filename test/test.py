import unittest
from TushareClient.api import isTodayOpen

class MyTestCase(unittest.TestCase):
    def test_something(self):
        print(isTodayOpen())


if __name__ == '__main__':
    unittest.main()
