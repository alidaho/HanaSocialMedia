from flask import Flask, render_template, url_for, request, session
from incFiles.userPy import GetData
from incFiles.fire import Fire
from incFiles.emailVal import EmailVery
from incFiles.checkUser import Check
import os
app = Flask(__name__)

s_login = ""

#Home Page
@app.route('/')
def index():
    return render_template('index.html')

#Register Page
@app.route('/register')
def register():
    return render_template('register.html')

#Authentication page
@app.route('/auth', methods=['POST'])
def user_auth():
    get_data = GetData()

    if request.method == 'POST':
        register_form = request.form
        email_ver = EmailVery(register_form['email'])

        if(email_ver.email_valid() == True): #Check if email exists (Real Email)
            #email_ver.send_code()

            if(register_form['psw'] == register_form['psw-repeat']): #Check password if it matches
                firebase = Fire()
                if(not firebase.check_user_existence(register_form['email'],
                        register_form['username'], register_form['name'])): #Check if user exists or not
                    firebase.add_user(register_form)
                    get_data.get_data_from_html(register_form)
                    return register_form
                else:
                    return "User already exists"
            else:
                return "Password do not match"
        else:
            return "Email do not exist"


#Login Page
@app.route('/login')
def login():
    return render_template('login.html')

#Send code to the email
@app.route('/sent', methods = ['POST'])
def sent():
    login_form = request.form
    check_user = Check(login_form)
    if(check_user.check_email_existence()):
        if(check_user.check_password(login_form['password'])):
            fire = Fire()
            fire.get_token_id(login_form['email'], login_form['password'])
            s_login = login_form['email']
            return render_template('sent.html')
        else:
            return "Password wrong"
    else:
        return "Wrong"

def create_session(email):
    pass

#Home page after login
@app.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
