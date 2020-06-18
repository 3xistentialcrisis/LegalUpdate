from . import db
from werkzeug.security import (generate_password_hash,
                               check_password_hash)
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def user_loader(client_id):
    return Client.query.get(int(client_id))

class Case(db.Model):
    __tablename__ = "cases"

    case_id = db.Column(db.Integer,primary_key = True)
    case_title = db.Column(db.String)
    case_content = db.Column(db.String)
    posted_at = db.Column(db.DateTime,default=datetime.utcnow)
    category = db.Column(db.String)
    client_id = db.Column(db.Integer,db.ForeignKey("clients.id"))
    comments = db.relationship("Comment",backref = "case_comments",lazy = "dynamic")

    def save_case(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_user_cases(cls,id):
        cases = Case.query.filter_by(client_id = id).all()
        return cases

   
    def get_all_cases(cls):
        return Case.query.order_by(Case.posted_at.asc()).all()

class Comment(db.Model):
    __tablename__ = "comments"

    comment_id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    posted_at = db.Column(db.DateTime,default=datetime.utcnow)
    case_id = db.Column(db.Integer,db.ForeignKey("cases.case_id"))
    client_id = db.Column(db.Integer,db.ForeignKey("clients.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Case.query.filter_by(case_id = id).all()
        return comments

class Client(UserMixin, db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer,primary_key = True)
    full_name = db.Column(db.String(255))
    username = db.Column(db.String(255), unique = True)
    email = db.Column(db.String(255), unique = True, index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    cases = db.relationship("Case",backref = "cases",lazy = "dynamic")
    comments = db.relationship("Comment",backref = "comments",lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError("You cannot read the password attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # string representaion to print out a row of a column, important in debugging
    def __repr__(self):
        return f'Client {self.username}'



