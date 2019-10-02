from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://tushar:Krishcu12%40@cluster0-d2vx4.mongodb.net/test?retryWrites=true&w=majority")
database = client.BlockChain
username = "user3"
record = database.users.find({"username": username})
if record is not None:
    print("Database is connected")
else:
    print("None")
