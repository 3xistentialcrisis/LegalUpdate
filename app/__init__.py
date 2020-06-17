from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads
from flask_bootstrap import Bootstrap
from config import config_options, DevConfig
from flask_mail import Mail
from flask_simplemde import SimpleMDE

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
simple = SimpleMDE()



def create_app(config_name):
    
    app = Flask(__name__)
    
    #app configurations
    app.config.from_object(config_options[config_name])
    
    
     # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    simple.init_app(app)
    # Setting up configuration
    app.config.from_object(DevConfig)
    
    
    #registering the main app Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    #registering the auth blueprint
    from .auth import auth as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix = '/auth')
    
    return app