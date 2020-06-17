from flask import render_template, redirect,url_for, flash, request
from ..models import Client
from . import auth
from flask_login import login_user, login_required, logout_client, current_client
from ..import db
from .forms import RegistrationForm, LoginForm, ResetPassword, NewPassword
import os

@auth.route('/login',methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    login_form = LoginForm()
    
    if login_form.validate_on_submit():
        Client = Client.query.filter_by(email = login_form.email.data).first()
        if client is not None and client.verify_password(login_form.password.data):
            login_client(client, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.home'))
        
        flash('Invalid client_clientname or password')
        
    title = "Login | Client information"
    return render_template('auth/login.html', login_form = login_form, title = title)


@auth.route('/register',methods = ['GET', 'POST'])
def register():
    if current_client.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        client = client(email = form.email.data, client_clientname = form.client_clientname.data, password = form.password.data)
        db.session.add(client)
        db.session.commit()
        
        
        return redirect(url_for('auth.login'))
    
    title = "New Account | Client information"
    
    return render_template('auth/register.html', registration_form = form, title = title)


@auth.route('/logout')
@login_required
def logout():
    logout_client()
    
    return redirect(url_for('main.index'))

@auth.route('/reset', methods = ['GET', 'POST'])
def reset_password():
    if current_client.is_authenticated:
        return redirect(url_for('main.index'))
    form = ResetPassword()
    if form.validate_on_submit():
        client = client.query.filter_by(email=form.email.data).first()
        if client:
            send_reset_email(client)
            flash('Check your email on how to reset password')
            return redirect(url_for('auth.login'))
        elif not user:
            flash('Your email does not exist!')
    return render_template('auth/reset.html',title='Reset Password',form=form)


@auth.route('/new_password/<token>', methods=['GET','POST'])
def new_password(token):
    if current_client.is_authenticated:
        return redirect(url_for('main.index'))
    client = Client.verify_reset_password(token)
    if not client:
        return redirect(url_for('main.index'))
    form = NewPassword()
    if form.validate_on_submit():
        client.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset')
        return redirect(url_for('auth.login'))
    return render_template('auth/change_password.html',title='Reset Password',form=form)

