import os
from pymongo import MongoClient
from google.cloud import storage


mongo_client = MongoClient("mongodb+srv://tushar:Krishcu12%40@cluster0-d2vx4.mongodb.net/admin?retryWrites=true&w=majority")
database = mongo_client.BlockChain
record = database.users.find({"email":"testuser1"})
if record is not None:
    print("MongoDB database is Connected")
    # print(record.__dict__)

arr = os.listdir()
if 'serviceAccount.json' in arr:
    print('Google Cloud Storage is Connected')
    rawPath = "serviceAccount.json"
    client = storage.Client.from_service_account_json(rawPath)
    bucket_name = 'nyclibrary_bucket'
    bucket = client.get_bucket(bucket_name)
else:
    print('serviceAccount.json not found!')
