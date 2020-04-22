
from userPy import User
import json as js

def main():

    users = User(12, "Ali", 24, "alildb", "azerty92421276", "607-353-3197", "larbidaoa@gmail.com")

    users.create_client()

    userId = users.add_user()

    print(userId.inserted_id)

    users.printDBInfo()

def getDataForm():
    print("Done...")


#Run Main function
if __name__ == "__main__":
    main()
