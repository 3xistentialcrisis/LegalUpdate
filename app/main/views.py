from flask import render_template, request, redirect, url_for, flash, abort
from . import main
from ..models import Client, Case, Comment
from flask_login import login_required, current_client
from .. import db
from .forms import CaseForm, CommentForm, UpdateProfile
import markdown2

@main.route('/')
def index():
    '''
    root page function that returns the index page and it's data
    '''
    title = "Welcome to Legal_Update"

    return render_template("index.html", title=title)

@main.route('/client/<cname>&<id_client>')
@login_required
def profile(cname, id_client):
    client = Client.query.filter_by(clientname = cname).first()

    title = f"{cname.capitalize()}'s Profile"

    get_cases = case.query.filter_by(client_id = id_client).all()
    get_comments = Comment.query.filter_by(client_id = id_client).all()

    if client is None:
        abort(404)
    
    return render_template('profile/profile.html', client = client, title=title, cases_no = get_cases, comments_no = get_comments)


@main.route('/home', methods = ['GET', 'POST'])
@login_required
def home():
    client_form = ClientForm()
    
    if client_form.validate_on_submit():
        case = case_form.case.data
        cat = case_form.my_category.data

        new_case = Case(case_content=case, case_category = cat, client = current_client)
        new_case.save_case()

        return redirect(url_for('main.home'))

    all_cases = Cases.get_all_cases()

    title = "Home"    
    return render_template('home.html', title = title, case_form = case_form, cases = all_cases)

@main.route('/case/<int:id>',methods = ['GET','POST'])
@login_required
def case(id):
    
    my_case = Case.query.get(id)
    comment_form = CommentForm()
    
    if id is None:
        abort(404)

    if comment_form.validate_on_submit():
        comment_data = comment_form.comment.data
        new_comment = Comment(comment_content = comment_data, case_id = id, client = current_client)
        new_comment.save_comment()

        return redirect(url_for('main.case',id=id))

    all_comments = Comment.get_comments(id)


    title = "Comment"
    return render_template('case.html',case = my_case, comment_form = comment_form, comments = all_comments, title = title)

@main.route('/category/<cat>')
def category(cat):
    my_category = case.get_category(cat)

    title = f'{cat} category'

    return render_template('category.html', title=title, category=my_category)

@main.route('/client/<cname>/update', methods=['GET','POST'])
@login_required
def update_profile(cname):
    client= Client.query.filter_by(clientname = cname).first()

    if client is None:
        abort(404)
    
    update_form = UpdateProfile()

    if update_form.validate_on_submit():
        user.bio = update_form.bio.data
        db.session.add(client)
        db.session.commit()

        return redirect(url_for('.profile',cname = client.clientname,id_client=client.id))
    title = 'Update Bio'
    return render_template('profile/update.html', form=update_form, title = title)
