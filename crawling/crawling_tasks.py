from background_task import background
import time
import requests;
from bs4 import BeautifulSoup;
from pymongo import MongoClient
import pandas as pd



@background()
def task_crawling_trade(schedule=5, repeat=60*60*24*30):

    BgnDe = []
    EndDe = []
    for year in range(2011,2021):
        BgnDe.append(str(year)+'01')    # 201101,201201,...,202001
        EndDe.append(str(year)+'12')    # 201112,201212,...,202012
        # BgnDe.(str(year)+str(month)) # per month

    hs = pd.read_csv('HS_CODE.csv')
    ItemCd = []
    for i in range(len(hs)):
        hs_code = hs.iloc[i]
        ItemCd.append(hs_code)

    for a in BgnDe:
        for b in EndDe:
            for c in ItemCd:
                res = requests.get(
                    'http://openapi.customs.go.kr/openapi/service/newTradestatistics/getitemtradeList?serviceKey=T%2FkSHIT8tHIywdhJYJpQfEGJnITSvR1P0jMOloSBrgnY4xW9ijW5C7EWwSR%2B%2FPe15lQ5yIBffQ%2BHiRJDTwRMTw%3D%3D'
                    +'&searchBgnDe='+BgnDe[a]
                    +'&searchEndDe='+EndDe[b]
                    +'&searchItemCd='+ItemCd[c]
                )

    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser')
        with MongoClient.connect("mongodb://172.17.0.2:27017/") as client:
            cur = client.cursor()
            cur.execute("db.KOR.insert({year:"1"},{expDlr:"1"},{impDlr:"1"},{balPayments:"1"},{expCnt:"1"},{impCnt:"1"},{totalCount:"1"})", (title, link))
            con.commit()
            client.close()
        print('task_crawling_trade: ', type(links), len(links))

    time_tuple = time.localtime()
    time_str = time.strftime("%m/%d/%Y, %H:%M:%S", time_tuple)
    print('task_crawling_trade: ', type(links), len(links), time_str
        
        
client = MongoClient('mongodb://172.17.0.2:27017/') # with Docker inspect
tradedb = client.tradedb # get Database
# data = {'title': 'mariaDB 보기', 'tags': ['디비 서비스']}
KOR_info = tradedb.KOR.insert_one(data)
# data = [ {"name": "Ram", "age": "26", "city": "Hyderabad"},
# {"name": "Rahim", "age": "27", "city": "Bangalore"}]
res = mydb.board.insert_many(data); 
print(res.inserted_ids)

KOR_info = tradedb.KOR.find() # get Collection with find()
for info in KOR_info: # Cursor
    print(info)

client.close()
    # add Crawling and insert to DB previously Code
    time_tuple = time.localtime()
    time_str = time.strftime("%m/%d/%Y, %H:%M:%S", time_tuple)
    print('task_crawling_daum: ', type(links), len(links), time_str)

