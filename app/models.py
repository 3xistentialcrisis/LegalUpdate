from . import db, login_manager
from flask_login import current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

#Add Class User and Class Role


#Save Client's Files
class Files(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(255), unique=True, nullable=False)
    file_name = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    type = db.Column(db.String(255), unique=True, nullable=False)
    date_created = db.Column(db.String(255), unique=True, nullable=False)

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
