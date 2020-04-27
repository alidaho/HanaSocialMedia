from flask import Flask, render_template, url_for, request
from incFiles.userPy import GetData
from incFiles.fire import Fire
from incFiles.emailVal import EmailVery
app = Flask(__name__)


#Home Page
@app.route('/')
def index():
    return render_template('index.html')

#Register Page
@app.route('/register')
def register():
    return render_template('register.html')

#Send code to the email
@app.route('/sent', methods = ['POST'])
def sent():
    return render_template('sent.html', register_form=register_form)

#Login Page
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def user_auth():
    get_data = GetData()

    if request.method == 'POST':
        register_form = request.form
        email_ver = EmailVery(register_form['email'])

        if(email_ver.email_valid() == True): #Check if email exists (Real Email)
            #email_ver.send_code()

            if(register_form['psw'] == register_form['psw-repeat']): #Check password if it matches
                firebase = Fire("zumi", "users", register_form['username'])
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




if __name__ == "__main__":
    app.run(debug=True, port=5000)
