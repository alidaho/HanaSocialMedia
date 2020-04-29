import firebase_admin
from firebase_admin import auth, db, firestore, credentials
import google.cloud
from google.cloud.firestore_v1 import Increment
import numpy as np

db = firestore.client()
doc_ref = db.collection(u'users')


class Check:
    def __init__(self, data):
        self.data = data

            #Check email existence
            #Do not forget to call it in app.register.py
    def check_email_existence(self):
        doc = doc_ref.document(self.data['email'])
        check = doc.get()
        if check.exists:
            print(u'Document data: {}'.format(check.to_dict()))
            return check.to_dict()
        else:
            print(u'No such document')
            return False

        #Pass key and value and return if data exists or not
    def do_you_exists(self, data_key, new_value):
        return True

            #Check Username existence
    def check_username(self, new_username):
        if (self.do_you_exists('username', new_username)):
            print("Everything cool")
            return True
        else:
            print("everything messed up")
            return False

            #Check password existence
    def check_password(self, new_password):
        new_data = self.check_email_existence()
        print(new_data)
        if (new_data['psw'] == new_password):
            print("Everything cool")
            return True
        else:
           print("everything messed up")
           return False


        #This function is made to save token and make only login user use it
    def get_token(self, token):
        pass

        #Sending email works only once website is deployed
    def send_code(self, message, email):
        code = 0;
        return code

    def check_code(self, email, new_code):
        message = "This is your code: "
        email = "alildb2036@gmail.com"
        checkup = self.send_code(msg, email)

    def match_up(self):
        pass
