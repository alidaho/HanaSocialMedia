from validate_email import validate_email
import random
import smtplib
from smtplib import SMTPException
#import socket

class EmailVery:
    def __init__(self, email):
        self.email = email

    def email_valid(self):
        is_valid = validate_email(self.email, check_mx=True, verify=True)
        return is_valid

    def send_code(self):

        sender = "teratech19@gmail.com"
        receivers = self.email

        message = """From : From Zumi <zumisho@zumi.com>
        To: To <alildb@gmail.com>
        Subject: Welcome To Zumi

        Please activate your account with this code: 121544879415
                  """

        try:
            smtpObj = smtplib.SMTP('127.0.0.1:5000')
            smtpObj.sendmail(sender, receivers, message)
            print("Succeed")
        except SMTPException:
            print("Error: unable to send email")
