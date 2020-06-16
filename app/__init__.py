from flask import Flask
from config import config_options

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    #Create App Configurations
    app.config.from_object(config_options[config_name])
    app.config['SECRET_KEY'] = 'paper'

    #Register App Blueprints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #Initialise Flask Extensions
    db.init_app(app)


    return app