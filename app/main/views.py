from flask import (render_template, request, redirect, 
                   url_for, abort,flash)
from . import main
from .forms import CaseForm, CommentForm, UpdateProfile, CreateStatus
from ..models import Client, Comment, Case, Lawyers, Status
from flask_login import login_required, current_user
from .. import db, photos
from ..email import mail_message
import secrets
import os

@main.route("/", methods = ["GET", "POST"])
@login_required
def index():
    """
    View root page function that returns the index page and its data
    """
    all_cases = Case.query.all()
    case_form = CaseForm()
    title = "Legal Update | Leave a mark"

    if case_form.validate_on_submit():
        case_title = case_form.title.data
        case_form.title.data = ""
        case_content = case_form.case.data
        case_form.case.data = ""
        case_category = case_form.category.data
        new_case = Case(case_title = case_title,
                        case_content = case_content,
                        category = case_category,
                        )

        new_case.save_case()
        return redirect(url_for("main.index"))
    
    return render_template("index.html",
                            title = title,
                            case_form = case_form,
                            all_cases = all_cases)

 #Client Commenting on their File/Case
@main.route("/post/<int:id>", methods = ["GET", "POST"])
def case(id):
    client = Client.query.filter_by(id = id).first()
    case = Case.query.filter_by(case_id = id).first()
    title = case.case_title
    comments = Comment.query.filter_by(case_id = id).all()
    comment_form = CommentForm()

    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        comment_form.comment.data = ""
        new_comment = Comment(comment = comment, 
                            case_id = id,
                            client_id = id)
        new_comment.save_comment()
        return redirect(url_for("main.post", id = case.case_id))

    return render_template("post.html",
                            case = case,
                            title = title,
                            comments = comments,
                            comment_form = comment_form,
                            client = client)

 #Client Profile
@main.route("/profile/<int:id>/")
def profile(id):
    client = Client.query.filter_by(id = id).first()
    cases = Case.query.filter_by(client_id = id).all()
    title = client.full_name

    return render_template("profile/profile.html",
                            client = client,
                            cases = cases,
                            title = title)

 #Client Updating their Profile 
@main.route("/profile/<int:id>/update", methods = ["GET", "POST"])
def update(id):
    client = Client.query.filter_by(id = id).first()
    title = client.full_name
    if client is None:
        abort(404)

    form = UpdateProfile()
    if form.validate_on_submit():
        client.bio = form.bio.data
        db.session.add(client)
        db.session.commit()
        return redirect(url_for("main.profile",
                                id = id))

    return render_template("profile/update.html",
                            form = form,
                            client = client,
                            title = title)

 #Client Updating Profile Pic
@main.route("/profile/<int:id>/update/pic", methods = ["POST"])
def update_pic(id):
    client = Client.query.filter_by(id = id).first()
    if "photo" in request.files:
        filename = photos.save(request.files["photo"])
        path = f"photos/{filename}"
        client.profile_pic_path = path
        db.session.commit()
    return redirect(url_for("main.update",
                                id = id))

#Searching Clients
@main.route("/clients")
def clients():
    client = Client.query.all()
    title = "Browse clients"
    return render_template("clients.html", 
                            client = client,
                            title = title)

 #Searching Cases 
@main.route("/category/<cname>")
def category(cname):
    cases = Case.query.filter_by(category = cname).all()
    title = cname

    return render_template("category.html",
                            title = title,
                            cases = cases)
#About Page
@main.route("/about")
def about():
    title = "About Legal Update"
    return render_template("about.html",
                            title = title)
    

#Lawyer Create New File Status
@main.route('/new_post', methods=['POST','GET'])
@login_required
def new_status():
    files = Files.query.all()
    form = CreateStatus()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        lawyer_email = form.lawyer_email.data
        new_status = Status(title=title,content=content, lawyer_email=lawyer_email)
        new_status.save()


        for client in Clients:
            mail_message("A New Status Update has been made on your File", "email/new_status", client.email, new_status=new_status)
        return redirect(url_for('main.index'))
        flash('You Posted a new Status', danger)

    return render_template('newstatus.html', form = form)

#Lawyer Delete Status
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
  
  # #Create New Client File
# @main.route('/new_file', methods=['POST','GET'])
# @login_required
# def new_file():
#     clients = Client.query.all()
#     form = CreateFile()
#     if form.validate_on_submit():
#         client_name= form.client_name.data
#         file_name = form.file_name.data
#         file_type = form.file_type.data
#         lawyer_email = form.lawyer_email.data

#         new_file = CreateFile(client_name=client_name, file_name =file_name,
#                               file_type = file_type, lawyer_email=lawyer_email)
#         new_file.save()

#         for client in Clients:
#             return redirect(url_for('main.index'))
#         flash('You have created a New File')
#     return render_template('newfile.html', form = form)


