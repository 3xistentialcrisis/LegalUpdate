from . import db, login_manager
from flask_login import ClientMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from sqlalchemy import text
import jwt

@login_manager.lawyer_loader
def load_lawyer(lawyer_name):
    return Lawyers.query.get(lawyer_name)


#Save Lawyers
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

#Save Files
class Files(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.Integer, primary_key=True)
    clientname = db.relationship('Client Name', backref='clients', lazy='dynamic')
    file_name = db.Column(db.String(255), unique=True, nullable=False)
    file_type = db.Column(db.String(255), unique=True, nullable=False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def get_file(id):
        file = Files.query.all(id=id)

        return file

    def __repr__(self):
        return f'Files {self.client_name}'

#Save Client's Status
class Status(db.Model):
    __tablename = 'status'
    id = db.Column(db.Integer, primary_key=True)
    clientname = db.relationship('Client Name', backref='clients', lazy='dynamic')
    file_name = db.relationship('Client File', backref='Files', lazy='dynamic')
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