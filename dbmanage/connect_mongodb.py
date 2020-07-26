# class MongoDBPipeline(object):

#     def __init__(self):
#         connection = pymongo.MongoClient(
#             settings['MONGODB_SERVER'],
#             settings['MONGODB_PORT']
#         )
#         db = connection[settings['MONGODB_DB']]
#         self.collection = db[settings['MONGODB_COLLECTION']]

#     def process_item(self, item, spider):
#         for data in item:
#             if not data:
#                 raise DropItem("Missing data!")
#         self.collection.update({'url': item['url']}, dict(item), upsert=True)
#         log.msg("Question added to MongoDB database!",
#                 level=log.DEBUG, spider=spider)
#         return item



from pymongo import MongoClient
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
