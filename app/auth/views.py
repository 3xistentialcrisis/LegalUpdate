from flask import render_template,flash, request, redirect, url_for
from flask_login import login_user, logout_user,login_required
from app import db
from app.auth import auth
from app.models import Lawyers, Client
from .forms import RegistrationForm,LoginForm
from ..email import mail_message

#View Registration Form
@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        lawyer = Lawyers(email=form.lawyer_email.data, username=form.lawyer_name.data, department=form.department.data, password=form.password.data)
        db.session.add(lawyer)
        db.session.commit()
        mail_message("Welcome to Legal Update", "email/welcome", lawyer.lawyer_emailemail, lawyer=lawyer)

        return redirect(url_for('auth.lawyer_login'))
        title = "New Account"
    return render_template('auth/lawyer_register.html', registration_form=form)


#View Login Form
@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        lawyer = Lawyers.query.filter_by(email=login_form.email.data).first()
        if lawyer is not None and Lawyers.verify_password(login_form.password.data):
            login_user(lawyer, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Legalupdate login"
    return render_template('auth/lawyer_login.html', login_form=login_form, title=title)


#View Logout
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

    title = "Legalupdate logout"
    return render_template('auth/lawyer_login.html', title=title)