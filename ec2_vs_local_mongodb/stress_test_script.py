from pymongo import MongoClient
import time
client = MongoClient('mongodb+srv://quankhuc:kkquan226@cluster0.2gft4jx.mongodb.net/?retryWrites=true&w=majority')
all_databases = client.list_database_names()
collection = None
if 'test' in all_databases:
  print("Database test exists")
  collection = client['test']['stress_test']
else:
  print('Creating database test')
  db = client['test']
  collection = db['stress_test']
  collection.insert_one({'name': 'Quan', 'age': 22})

# 1000 insertions
start = time.time()
for i in range(1000):
  collection.insert_one({'name': 'Thanh', 'age': i})
end = time.time()
print('1000 insertions took {time:.2f} seconds'.format(time = end - start))

# 1000 selections
start = time.time()
for i in range(1000):
  collection.find_one({'name': 'Thanh', 'age': i})
end = time.time()
print('1000 selections took {time:.2f} seconds'.format(time = end - start))

# 1000 updates
start = time.time()
for i in range(1000):
  collection.update_one({'age': i}, {'$set': {'name': 'Khoa'}})
end = time.time()
print('1000 updates took {time:.2f} seconds'.format(time = end - start))

# 1000 deletions
start = time.time()
for i in range(1000):
  collection.delete_one({'age': i})
end = time.time()
print('1000 deletions took {time:.2f} seconds'.format(time = end - start))