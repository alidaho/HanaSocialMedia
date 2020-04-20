import pymongo as db

class db:
    def __init(self):
        pass
    def create_client(db_name, collection_name):
        myClient = db.MongoClient("mongodb://localhost:8080/")
        mydb = myClient[db_name]

        print(myClient.list_database_names()) #Print DB Name

        my_collection = mydb[collection_name] #Create Collection
        print(mydb.list_collection_names()) #Print Collection Name

    def delete_db(db_name):
        pass

    def update_db(db_name):
        pass
