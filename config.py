import os

class Config:

    QUOTES_API_KEY = 'http://quotes.stormconsultancy.co.uk/random.json'

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:joselyne@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    SUBJECT_PREFIX = 'Pitch-app'
    SENDER_EMAIL = 'joselynejojo740@gmail.com'

    @staticmethod
    def init_app(app):
        pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://sfvvmmpzhujazt:ec63a6b0d69d77704df34144e0262495a80ac6d39e8afddb8e5b43df33ed2029@ec2-54-160-202-3.compute-1.amazonaws.com:5432/deuua7g3sa6r8r
'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")



class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://sfvvmmpzhujazt:ec63a6b0d69d77704df34144e0262495a80ac6d39e8afddb8e5b43df33ed2029@ec2-54-160-202-3.compute-1.amazonaws.com:5432/deuua7g3sa6r8r
'
    DEBUG = True


    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
