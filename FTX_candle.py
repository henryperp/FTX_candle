from typing import Dict
import requests
from datetime import datetime


path = 'FTX_candle.txt'

Market = 'BTC'
Start = int(datetime(2020, 1, 1, 0, 0).timestamp())


End = int(datetime.now().timestamp())
x = 0
Start2 = Start

while x < 999 :
    Time0 = Start + x * (3600000 + 3600)
    Time1 = Start + (x+1) * (3600000 + 3600)

    if Time1 >= End :
        Time1 = End
        x = 1000

    print(f'Time0: {Time0}  Time1: {Time1}, End {End}')
    URL = 'https://ftx.com/api/indexes/'+  Market + '/candles?resolution=3600&start_time=' + str(Time0) + '&end_time=' + str(Time1)
    resp_F = (requests.get(URL)).json()
    
    for i in range(len(resp_F['result'])):
        f = open(path, 'a')
        li = resp_F['result'][i]['startTime']," ", str(resp_F['result'][i]['open']), " ",str(resp_F['result'][i]['high']), " ",str(resp_F['result'][i]['low']) ," ",str(resp_F['result'][i]['close']),'\n'
        f.writelines(li)
        #f.write(resp_F['result'][i]['startTime'])
        f.close()
    x = x +1

print('OK')
