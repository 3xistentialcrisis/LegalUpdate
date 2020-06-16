from flask import render_template,flash, request, redirect, url_for
from flask_login import login_user, logout_user,login_required
from app import db
from app.auth import auth
from app.models import User
from .forms import RegForm,LoginForm
from ..email import mail_message

#View Login Page
@auth.route('/login',methods = ['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user != None and user.verify_password(form.password.data):
            login_user(user, form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Wrong Username or Password')
    return render_template('auth/login.html',form = form)

#View Signup Page
@auth.route('/signup',methods = ["POST","GET"])
def signup():
    form = RegForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        user.save()
        db.session.add(user)
        db.session.commit()
        mail_message("Welcome to Legal Update!", "email/welcome", user.email, user=user)
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html', registration_form=form)

#User Logout
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
