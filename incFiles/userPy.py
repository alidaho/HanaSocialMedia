import pymongo as db
import random as rn
import json as js
from dbCreation import *

class User:
    def __init(self, name, id, pwd, phone, email):
        name = self.name
        id = self.id
        pwd = self.pwd
        phone = self.phone
        email = self.email

    def add_user(self):
        #Store user data into dictionary
        user_info = {
            "name"  : self.name,
            "age"   : self.age,
            "id"    : self.id,
            "pwd"   : self.pwd,
            "phone" : self.phone,
            "email" : self.email
        }

    def delete_account(self):
        pass
    def email_verification(self):
        code = ""
        return code
