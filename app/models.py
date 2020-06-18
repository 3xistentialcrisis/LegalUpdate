from . import db
from werkzeug.security import (generate_password_hash,
                               check_password_hash)
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from datetime import datetime
from sqlalchemy import text


#Lawyer
@login_manager.user_loader
def user_loader(lawyer_id):
    return Lawyers.query.get(int(lawyer_id))


# Lawyer Details
class Lawyers(UserMixin, db.Model):
    __tablename__ = 'lawyers'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255))
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    department = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    cases = db.relationship("Case", backref="cases", lazy="dynamic")

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
        return f'Lawyers {self.username}'


#Cases/Files
class Case(db.Model):
    __tablename__ = "cases"

    case_id = db.Column(db.Integer,primary_key = True)
    client_name = db.Column(db.String)
    case_title = db.Column(db.String)
    case_content = db.Column(db.String)
    posted_at = db.Column(db.DateTime,default=datetime.utcnow)
    category = db.Column(db.String)
    lawyer_id = db.Column(db.Integer,db.ForeignKey("lawyers.id"))


    def save_case(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_user_cases(cls,id):
        cases = Case.query.filter_by(lawyer_id = id).all()
        return cases

    def get_all_cases(cls):
        return Case.query.order_by(Case.posted_at.asc()).all()


#Save File Status
class Status(db.Model):
    __tablename = 'status'
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(255))
    case_title = db.Column(db.String(255))
    title = db.Column(db.String)
    content = db.Column(db.String)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

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
