from pymongo import MongoClient

def searchUser(item) :
    cluster = MongoClient("mongodb+srv://anand:1234@googlereviewscloneproje.gdul8xz.mongodb.net/?retryWrites=true&w=majority")
    print(cluster.list_database_names())
    db = cluster["ReviewCloneProject"]
    collection = db["UserDetails"]
    query = dict()
    query[item] = 1
    result = collection.find({}, query)
    for x in result :
        print(x[item])

if __name__ == "__main__" :
    searchUser("Username")