import unittest
import tushare as ts
import pandas

class MyTestCase(unittest.TestCase):
    def test_something(self):
        from datetime import date
        pro = ts.pro_api('65a2791eeac8d57edc1d3b0bfebbc902b4c085564530d8fe29f6d4a9')
        today = date.today().__str__().replace('-', '')
        df = pro.trade_cal(exchange='SSE', start_date=today, end_date=today)
        print(df)


if __name__ == '__main__':
    unittest.main()
