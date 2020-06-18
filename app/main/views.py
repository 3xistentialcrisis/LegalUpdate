from flask import (render_template, request, redirect, 
                   url_for, abort)
from . import main
from .forms import CaseForm, CommentForm, UpdateProfile
from ..models import Client, Comment, Case
from flask_login import login_required, current_user
from .. import db, photos

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

@main.route("/profile/<int:id>/")
def profile(id):
    client = Client.query.filter_by(id = id).first()
    cases = Case.query.filter_by(client_id = id).all()
    title = client.full_name

    return render_template("profile/profile.html",
                            client = client,
                            cases = cases,
                            title = title)

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

@main.route("/clients")
def clients():
    client = Client.query.all()
    title = "Browse clients"
    return render_template("clients.html", 
                            client = client,
                            title = title)

@main.route("/category/<cname>")
def category(cname):
    cases = Case.query.filter_by(category = cname).all()
    title = cname

    return render_template("category.html",
                            title = title,
                            cases = cases)

@main.route("/about")
def about():
    title = "About Legal Update"
    return render_template("about.html",
                            title = title)
    

