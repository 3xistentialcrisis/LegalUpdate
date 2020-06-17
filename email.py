from flask_mail import Message
from manage import app
from . import mail
from flask import render_template
import os

def send_email(subject, sender, recepients, text_body, html_body):
    msg = Message(subject,sender=sender,recipients=recepients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)

def send_reset_email(user):
    token = client.get_reset_password_token()
    send_email('Reset Password',sender=app.config['MAIL_CLIENTNAME'],recepients=[client.email],text_body=render_template('auth/reset_password.txt',client=client, token=token),html_body=render_template('auth/reset_password.html',client=client, token=token))