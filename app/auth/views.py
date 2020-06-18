
from flask import (render_template, redirect, url_for,
                  flash, request)
from flask_login import login_user, logout_user, login_required
from . import auth
from ..models import Client, Lawyers
from .forms import SignUpForm, LoginForm
from .. import db
from ..email import mail_message

#Client Signup View
@auth.route("/signup", methods = ["GET", "POST"])
def register():
    signup_form = SignUpForm()
    if signup_form.validate_on_submit():
        client = Client(full_name = signup_form.full_name.data, 
                    username = signup_form.username.data, 
                    email = signup_form.email.data,
                    password = signup_form.password.data)
        db.session.add(client)
        db.session.commit()

        mail_message("Welcome to Legal Update",
                     "email/welcome", client.email, client = client)
        return redirect(url_for("auth.login"))
    title = "Sign Up to 60 Seconds"
    return render_template("auth/signup.html", 
                            signup_form = signup_form,
                            title = title)

#Client Login View
@auth.route("/login", methods = ["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        client = Client.query.filter_by(email = login_form.email.data).first()
        if client is not None and client.verify_password(login_form.password.data):
            login_user(client, login_form.remember.data)
            return redirect(request.args.get("next") or url_for("main.index"))

        flash("Invalid Username or Password")
    
    title = "Login to Legal Update"
    return render_template("auth/login.html",
                            login_form = login_form,
                            title = title)
#Client Logout
@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

#Lawyer SignUp View
@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        lawyer = Lawyers(email=form.lawyer_email.data, username=form.lawyer_name.data, department=form.department.data, password=form.password.data)
        db.session.add(lawyer)
        db.session.commit()
        mail_message("Welcome to Legal Update", "email/welcome", lawyer.lawyer_email, lawyer=lawyer)

        return redirect(url_for('auth.lawyer_login'))
        title = "New Account"
    return render_template('auth/lawyer_register.html', registration_form=form)


#Lawyer Login View
@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LawyerLoginForm()
    if login_form.validate_on_submit():
        lawyer = Lawyers.query.filter_by(email=login_form.email.data).first()
        if lawyer is not None and Lawyers.verify_password(login_form.password.data):
            login_user(lawyer, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Legalupdate login"
    return render_template('auth/lawyer_login.html', login_form=login_form, title=title)


#Lawyer Logout
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

    title = "Legalupdate logout"
    return render_template('auth/lawyer_login.html', title=title)
