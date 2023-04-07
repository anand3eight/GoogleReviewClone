import ssl
import pymongo
from pymongo import MongoClient

def insertUser(user) :
    cluster = MongoClient("mongodb+srv://anand:1234@googlereviewscloneproje.gdul8xz.mongodb.net/?retryWrites=true&w=majority")
    print(cluster.list_database_names())
    db = cluster["ReviewCloneProject"]
    collection = db["UserDetails"]
    collection.insert_one(user)
    print('Insertion Successful')

if __name__ == "__main__" :
    user = dict()
    user['_id'] = 1
    user['name'] = 'Abe'
    user['Country'] = 'India'
    print(user)
    insertUser(user)
