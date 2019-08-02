import os
import config
from flask import Flask,flash,redirect,url_for
from models.base_model import db
from models.user import User
from flask_login import LoginManager,current_user,logout_user,login_required,login_user

web_dir = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'werkoot_web')

app = Flask('WERKOOT', root_path=web_dir)

if os.getenv('FLASK_ENV') == 'production':
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)

@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('users.show',username = current_user.username))
    else:
        flash('You are not logged in','warning')
        return redirect(url_for('sessions.new'))


@app.before_request
def before_request():
    db.connect()


@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        print(db)
        print(db.close())
    return exc
