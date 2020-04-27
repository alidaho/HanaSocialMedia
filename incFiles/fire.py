import firebase_admin
from firebase_admin import credentials, firestore, db
import google.cloud

cred = credentials.Certificate("path/zumish-a7a8c-firebase-adminsdk-djj1b-d969258375.json")
app = firebase_admin.initialize_app(cred)
store = firestore.client()
doc = store.collection(u'users')

class Fire:
    def __init__(self, collection, document, id):
        self.col = collection
        self.doc = document
        self.id = id

    def create_dir(self, username):
        doc_ref = doc.document(username)
        return doc_ref
    def add_user(self, data):
        d = self.create_dir(data['username'])
        d.set({
        u'username' : data['username'],
        u'email'    : data['email'],
        u'name'     : data['name'],
        u'psw'      : data['psw'],
        })

    def check_user_existence(self, email, username, name):
        print("Data: {}".format(doc.get()))
        return False
