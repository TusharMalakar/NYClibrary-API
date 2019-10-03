import os
from pymongo import MongoClient
from google.cloud import storage


mongo_client = MongoClient(
    "mongodb+srv://tushar:Krishcu12%40@cluster0-d2vx4.mongodb.net/test?retryWrites=true&w=majority")
database = mongo_client.NYClibrary

record = database.users.find({"username": "testuser1"})
if record is not None:
    print("Mongodb Database is Connected")
else:
    print("None")


arr = os.listdir()
if 'serviceAccount.json' in arr:
    print('Google Cloud Storage is Connected')
    rawPath = "serviceAccount.json"
    client = storage.Client.from_service_account_json(rawPath)
    bucket_name = 'nyclibrary_nucket'
    bucket = client.get_bucket(bucket_name)
else:
    print('serviceAccount.json not found!')
