from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import ClientMixin
from sqlalchemy import text
import jwt
import os

@login_manager.client_loader
def load_client(client_id):
    return Client.query.get(int(user_id))

class Client(ClientMixin, db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key = True)
    clientname = db.Column(db.String(255))
    hash_pass = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index = True)
    bio = db.Column(db.String(255))

    cases = db.relationship('Case',backref='client',lazy='dynamic')
    comments = db.relationship('Comment',backref='client',lazy='dynamic')
    
    @property
    def password(self):
        raise AttributeError("You can not read password attribute")
    
    @password.setter
    def password(self,password):
        self.hash_pass = generate_password_hash(password)
        
    def set_password(self, password):
        self.hash_pass = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.hash_pass, password)
    
    
    def __repr__(self):
        return f'Client {self.clientname}'
    
    
class Case(db.Model):
    __tablename__ = 'cases'
    
    id = db.Column(db.Integer, primary_key = True)
    case_content = db.Column(db.String())
    case_category = db.Column(db.String(255))
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    
    def save_case(self):
    db.session.add(self)
    db.session.commit()  
    @classmethod
    def get_case(cls,id):
        cases = Case.query.filter_by(id=id).all()
        return cases
    
    @classmethod
    def get_all_cases(cls):
        cases = Case.query.order_by(text('-id')).all()
        return cases
    
    @classmethod
    def get_category(cls, cat):
        category = Case.query.filter_by(case_category = cat).order_by(text('-id')).all()
        
        return category        
    

        
    
class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer,primary_key=True)
    comment_content = db.Column(db.String())
    pitch_id = db.Column(db.Integer)
    client_id = db.Column(db.Integer,db.ForeignKey('clients.id')) 
    
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
        
    
    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(case_id=id).all()
   