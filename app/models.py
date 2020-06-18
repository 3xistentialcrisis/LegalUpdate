from . import db, login_manager
from werkzeug.security import (generate_password_hash,
                               check_password_hash)
from flask_login import UserMixin, ClientMixin
from . import login_manager
from datetime import datetime
from datetime import datetime
from sqlalchemy import text
import jwt

#Client
@login_manager.user_loader
def user_loader(client_id):
    return Client.query.get(int(client_id))
#Lawyer
@login_manager.user_loader
def load_lawyer(lawyer_name):
    return Lawyers.query.get(lawyer_name)

#Clients Cases/Files
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

#Client Comment on Case/File   
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

#Client Details
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

#Lawyers Details
class Lawyers(db.Model):
    __tablename__= 'lawyers'

    id = db.Column(db.Integer,primary_key=True)
    lawyer_name = db.Column(db.String(255), unique=True, nullable=False)
    lawyer_email = db.Column(db.String(255),unique=True,index=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    department = db.Column(db.String(255), unique=True, nullable=False)

    @property
    def set_password(self):
        raise AttributeError('You cannot read the password attribute')

    @set_password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'Lawyers {self.lawyer_name}'

#Save Client's Status
class Status(db.Model):
    __tablename = 'status'
    id = db.Column(db.Integer, primary_key=True)
    clientname = db.relationship('Client Name', backref='client', lazy='dynamic')
    case_title = db.relationship('Client File', backref='case', lazy='dynamic')
    title = db.Column(db.String(255), unique=True, nullable=False)
    content = db.Column(db.String(255), unique=True, nullable=False)
    date_created = db.Column(db.String(255), unique=True, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def get_status(id):
        status = Status.query.all(id=id)

        return status

    def __repr__(self):
        return f'Status {self.file_name}'
        
# #Save Files
# class Files(db.Model):
#     __tablename__ = 'files'

#     id = db.Column(db.Integer, primary_key=True)
#     clientname = db.relationship('Client Name', backref='clients', lazy='dynamic')
#     file_name = db.Column(db.String(255), unique=True, nullable=False)
#     file_type = db.Column(db.String(255), unique=True, nullable=False)
#     date_created = db.Column(db.DateTime,default=datetime.utcnow)

#     def save(self):
#         db.session.add(self)
#         db.session.commit()

#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()

#     def get_file(id):
#         file = Files.query.all(id=id)

#         return file

#     def __repr__(self):
#         return f'Files {self.client_name}'




 

