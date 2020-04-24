import pymongo

class db:
    def __init__(self):
        pass
    def __init(self, myC, myDbs, myCollection):
        self.client = myC
        self.db = myDbs
        self.collection = myCollection

    def create_client(self):
        myClient = pymongo.MongoClient("127.0.0.1", 27017)
        mydb = myClient["hana"]

        my_collection = mydb["users"] #Create Collection

        self.client = myClient
        self.db = mydb
        self.collection = my_collection

    def delete_db(db_name):
        pass

    def update_db(db_name):
        pass

    def checkOut(self):
        pass

    def return_db(self):
        db_list = [self.client, self.db, self.collection]
        return db_list

    def printDBInfo(self):
        print("DB Name: " + str(self.client.list_database_names()))
        print("Collection Name: " + str(self.db.list_collection_names()))
