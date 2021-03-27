import unittest
import TushareClient.TushareClient as tsClient


class MyTestCase(unittest.TestCase):
    def test_something(self):
        from datetime import date
        tsc = tsClient.Client
        pro = tsc.__get__(tsc)
        today = date.today().__str__().replace('-', '')
        df = pro.trade_cal(exchange='SSE', start_date=today, end_date=today)
        print(df)


if __name__ == '__main__':
    unittest.main()
