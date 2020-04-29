from dbCreation import db

class Admin(db):

    def __init__(self):
        pass
    def __init__(self, name, id, pwd):
        self.name = name
        self.id = id
        self.pwd = pwd

    def check_admin(self, email, id, pwd):
        pass

    def admin_dec():
        pass

    def check_choice():
        choice = 0
        print("Choose 1 - 5")
        print("1. Print DB: ")
        print("2. Delete DB: ")
        choice = input("Choose: ")
        return choice

#Main Admin Function
def main():
    admin_act = Admin("larbidaoa@gmail.com", 123, "azerty92421276")
