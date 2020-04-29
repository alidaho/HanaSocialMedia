import pymongo as db
import random as rn
from incFiles.dbCreation import db

class User(db):
    def __init__(self, level, name, age, id, pwd, phone, email):
        self.level = level
        self.name = name
        self.age = age
        self.id = id
        self.pwd = pwd
        self.phone = phone
        self.email = email

    def __init__(self):
        pass

    def checkInfo(self):
        if not self.name:
            print("Enter Name Please")
        if not self.age:
            print("Enter Correct Age")
        if not self.pwd:
            print("Please Enter the Password")
        if not self.phone:
            print("Please Enter the Phone Number")
        if not self.email:
            print("Please Enter the Email")

    def add_user(self):
        #Store user data into dictionary
        user_info = {
            "level" : self.level,
            "name"  : self.name,
            "age"   : self.age,
            "id"    : self.id,
            "pwd"   : self.pwd,
            "phone" : self.phone,
            "email" : self.email
        }

        #Insert data into db:
        insertX = self.collection.insert_one(user_info)

        return insertX

    def user_exists(self, email, phone, id):
        check = False
        if (email == "" or phone == "" or id == 0):
            check = True
        return check

    def email_verification(self):
        code = ""
        return code

    def delete_account(self):
        pass

class GetData:
    def get_data_from_html(self,data):
        print(data)
