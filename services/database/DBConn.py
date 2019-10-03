from pymongo import MongoClient
from google.cloud import storage


client = MongoClient(
    "mongodb+srv://tushar:Krishcu12%40@cluster0-d2vx4.mongodb.net/test?retryWrites=true&w=majority")
database = client.NYClibrary
# username = "testuser1"
# record = database.users.find({"username": username})
# if record is not None:
#     print("Database is connected")
# else:
#     print("None")


rawPath = "serviceAccount.json"
client = storage.Client.from_service_account_json(rawPath)
bucket_name = 'nyclibrary_nucket'
bucket = client.get_bucket(bucket_name)


