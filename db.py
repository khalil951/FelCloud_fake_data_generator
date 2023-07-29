from pymongo.mongo_client import MongoClient
from bson import ObjectId
import os

secret_key = os.environ.get('secret_key')
# print(type(secret_key))
uri = "mongodb+srv://khalil:"+secret_key+"@cluster0.0azwkml.mongodb.net/my_database?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client['my_database']
collection = db['Personas']

# # Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print('successful connection to db')
except Exception as e:
    print(e)

def inject_db(file_name , csv):
    try:
        with open(file_name, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                collection.insert_one(row)
    except Exception as e:
            print(e)
    return collection       

def empty_one(id):
    collection.find_one_and_delete({"_id": ObjectId(id)})
    return collection

def update_one(id , ele , val):
     collection.find_one_and_update({"_id": ObjectId(id)} , {"$set" : {ele : val}})           