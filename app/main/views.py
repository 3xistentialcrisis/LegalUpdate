from flask import (render_template, request, redirect, 
                   url_for, abort,flash)
from . import main
from .forms import CaseForm, UpdateProfile, CreateStatus
from ..models import Case, Lawyers, Status
from flask_login import login_required, current_user
from .. import db
from ..email import mail_message

@main.route("/", methods = ["GET", "POST"])
@login_required
def index():
    """
    View root page function that returns the index page and its data
    """
    title = "About Legal Update"
    return render_template("index.html",
                           title=title)


#About Page
@main.route("/about")
def about():
    all_cases = Case.query.all()
    case_form = CaseForm()
    title = "Legal Update | Leave a mark"

    if case_form.validate_on_submit():
        case_title = case_form.title.data
        case_form.title.data = ""
        client_name = case_form.client_name.data
        case_form.client_name.data = ""
        case_content = case_form.case.data
        case_form.case_content.data = ""
        # case_form.case.data = ""
        case_category = case_form.category.data
        new_case = Case(case_title=case_title,
                        client_name=client_name,
                        case_content=case_content,
                        category=case_category,
                        )

        new_case.save_case()
        return redirect(url_for("main.index"))

    return render_template("about.html",
                           title=title,
                           case_form=case_form,
                           all_cases=all_cases)

#Lawyer Profile
@main.route("/profile/<int:id>/")
def profile(id):
    lawyer = Lawyers.query.filter_by(id = id).first()
    cases = Case.query.filter_by(case_id = id).all()
    title = lawyer.full_name

    return render_template("profile/profile.html",
                            lawyer = lawyer,
                            cases = cases,
                            title = title)

#Lawyer Updating their Profile
@main.route("/profile/<int:id>/update", methods = ["GET", "POST"])
def update(id):
    lawyer = Lawyers.query.filter_by(id = id).first()
    title = Lawyers.full_name
    if lawyer is None:
        abort(404)

    form = UpdateProfile()
    if form.validate_on_submit():
        lawyer.bio = form.bio.data
        db.session.add(lawyer)
        db.session.commit()
        return redirect(url_for("main.profile",
                                id = id))

    return render_template("profile/update.html",
                            form = form,
                            lawyer = lawyer,
                            title = title)

#Searching Lawyers
@main.route("/lawyers")
def lawyers():
    lawyer = Lawyers.query.all()
    title = "Browse lawyers"
    return render_template("lawyers.html",
                            lawyer = lawyer,
                            title = title)

#Searching Cases
@main.route("/category/<cname>")
def category(cname):
    cases = Case.query.filter_by(category = cname).all()
    title = cname

    return render_template("category.html",
                            title = title,
                            cases = cases)

    

#Lawyer Create New File Status
@main.route('/new_status', methods=['POST','GET'])
@login_required
def new_status():
    all_status = Status.query.all()
    status_form = CreateStatus()
    title = "Legal Update | Leave a mark"

    if status_form.validate_on_submit():
        title = status_form.title.data
        status_form.title.data = ""
        client_name = status_form.client_name.data
        status_form.client_name.data = ""
        case_title = status_form.case_title.data
        status_form.case_title.data = ""
        content = status_form.content.data
        status_form.content.data = ""
        new_status = Status(title=title,
                        client_name=client_name,
                        case_title=case_title,
                        content=content)

        new_status.save()
        return redirect(url_for("main.index"))

    return render_template("newstatus.html",
                           title=title,
                           status_form=status_form,
                           all_status=all_status)

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
    return redirect(url_for('newstatus.html'))
