from flask import render_template,redirect,url_for,abort,request,flash
from app.main import main
from app.models import Files, Status, Lawyers
from .forms import CreateFile, CreateStatus
from .. import db
from flask_login import login_required,current_user
from ..email import mail_message
import secrets
import os

#Index Page
@main.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    return render_template('index.html')


#Create New Client File
@main.route('/new_file', methods=['POST','GET'])
@login_required
def new_file():
    clients = Client.query.all()
    form = CreateFile()
    if form.validate_on_submit():
        client_name= form.title.data
        file_name = form.content.data
        file_type = form.content.data
        lawyer_email = form.content.data

        new_file = CreateFile(client_name=client_name, file_name =file_name, file_type = file_type, lawyer_email=lawyer_email)
        new_file.save()

        for client in Clients:
            return redirect(url_for('main.index'))
        flash('You have created a New File')
    return render_template('newfile.html', form = form)


#Create New File Status
@main.route('/new_post', methods=['POST','GET'])
@login_required
def new_status():
    files = Files.query.all()
    form = CreateStatus()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        lawyer_email = form.content.data
        new_status = Status(title=title,content=content, lawyer_email=lawyer_email)
        new_status.save()


        for client in Clients:
            mail_message("A New Status Update has been made on your File", "email/new_status", client.email, new_status=new_status)
        return redirect(url_for('main.index'))
        flash('You Posted a new Status', danger)

    return render_template('newstatus.html', form = form)

#Delete Status
@main.route('/status/<status_id>/delete', methods = ['POST'])
@login_required
def delete_status(status_id):
    status = Status.query.get(status_id)
    if Lawyers.user != current_user:
        abort(403)
    status.delete()
    db.session.commit()
    flash("You have Successfully deleted the status!")
    return redirect(url_for('lawyersdashboard.html'))