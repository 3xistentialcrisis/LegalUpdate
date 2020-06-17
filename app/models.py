from . import db, login_manager
from flask_login import current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

#Roles
class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def save(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.name}'

#Users
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    bio = db.Column(db.String(255),default ='My default Bio')
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    hashed_password = db.Column(db.String(255), nullable=False)

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
        return "User: %s" % str(self.username)


#Save Lawyers
class Lawyers(db.Model):
    __tablename__='lawyers'

    id = db.Column(db.Integer,primary_key=True)
    lawyer_name = db.Column(db.String(255), unique=True, nullable=False)
    lawyer_email = db.Column(db.String(255),unique=True,index=True)
    department = db.Column(db.String(255), unique=True, nullable=False)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Lawyers {self.lawyer_name}'

#Save Client's Files
class Files(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(255), unique=True, nullable=False)
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
    client_name = db.relationship('Client Name', backref='Client', lazy='dynamic')
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