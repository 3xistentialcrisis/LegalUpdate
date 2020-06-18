import os 

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://remmi:stephen@localhost/legalupdate"
    UPLOADED_PHOTOS_DEST = "app/static/photos"

    # email configurations
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME= os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://remmi:stephen@localhost/legalupdate_test"

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://remmi:stephen@localhost/legalupdate"
    DEBUG = True


config_options = {
    "development": DevConfig,
    "production": ProdConfig,
    "test": TestConfig
}