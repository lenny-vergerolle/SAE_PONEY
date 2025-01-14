from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap5
import os.path


db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap5()

def mkpath(p):
    return os.path.normpath(
        os.path.join(
            os.path.dirname(__file__),
            p))

def creer_app(config=None):
    
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///' + mkpath('../testdb.db'))
    app.url_map.strict_slashes = False
    app.config['SECRET_KEY'] = 'e9767196-4490-415a-8d42-1b16d2ad2a24'
    app.config['SECURITY_DEFAULT_REMEMBER_ME'] = False
    app.config['SECURITY_REGISTERABLE'] = False
    app.config['SECURITY_RECOVERABLE'] = False
    app.config['SECURITY_TRACKABLE'] = False
    app.config['SECURITY_CONFIRMABLE'] = False
    app.config['SECURITY_CHANGEABLE'] = False
    app.config['BOOTSTRAP_SERVE_LOCAL'] = True

    if config:
        app.config.update(config)
        
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "login"
    bootstrap.init_app(app)

    return app

app = creer_app()

@login_manager.user_loader
def load_user(user_id):
    return Utilisateur.query.get(int(user_id))

def app_pour_tests():
    """Configure app pour les tests"""
    return creer_app({'TESTING': True,'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:','SQLALCHEMY_TRACK_MODIFICATIONS': False})
