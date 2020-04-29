import firebase_admin
from firebase_admin import credentials, firestore, db, auth
import google.cloud
from google.cloud.firestore_v1 import Increment

cred = credentials.Certificate("path/zumish-a7a8c-firebase-adminsdk-djj1b-d969258375.json")
app = firebase_admin.initialize_app(cred)
store = firestore.client()
doc = store.collection(u'users')

class Fire:
    def __init__(self):
        pass


    def create_dir(self, username):
        doc_ref = doc.document(username)
        return doc_ref
    def add_user(self, data):
        d = self.create_dir(data['email'])
        d.set({
        u'id'        : Increment(1),
        u'username'  : data['username'],
        u'email'     : data['email'],
        u'name'      : data['name'],
        u'psw'       : data['psw'],
        u'token_id'  : 0,
        u'user_level': 0,
        u'phone_number'     : data['phone']
        })




    def check_user_existence(self, email, username, name):
        print("Data: {}".format(doc.get()))
        return False

    #Get token id to make user login and custom one.
    #Pass token id to a databse to a specific user.
    #Made the user read data
    def get_token_id(self, new_email, psw):
        token_id = ""
        additional_claim = {
            'premiumAccount' : True
        }

        try:
            user_login = auth.create_user(email=new_email, password=psw)
            #custom_tokenID = auth.create_custom_token(token_id)
        except:
            print("Something went wrong")
