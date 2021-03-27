import json

from django.http import HttpResponse

import TushareClient.TushareClient as tsClient
from datetime import date


def isTodayOpen(obj):
    tsc = tsClient.Client
    pro = tsc.__get__(tsc)
    today = date.today().__str__().replace('-', '')
    df = pro.trade_cal(exchange='SSE', start_date=today, end_date=today)['is_open']
    df = str(df)
    return HttpResponse(json.dumps({'is_open': df}))
