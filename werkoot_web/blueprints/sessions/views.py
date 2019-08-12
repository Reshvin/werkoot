from flask import Blueprint, render_template,request,redirect,url_for,flash
from models.user import User
from flask_login import current_user,login_user,logout_user
from werkzeug.security import generate_password_hash,check_password_hash


sessions_blueprint = Blueprint('sessions',
                            __name__,
                            template_folder='templates/sessions')


@sessions_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('new.html')


@sessions_blueprint.route('/', methods=['POST'])
def create():
    username = request.form.get('username')
    password = request.form.get('password')
    user= User.get_or_none(User.username == username)

    if not user:
        flash("Username does not exist",'warning')
        return redirect(url_for('home'))

    check_password = check_password_hash(user.password,password)

    if not check_password:
        flash("Incorrect password",'danger')
        return redirect(url_for('home'))
    

    login_user(user)
    flash(f'Welcome back {user.username}.','success')
    return redirect(url_for('users.show', username = username))


@sessions_blueprint.route('/<username>', methods=["GET"])
def show(username):
    pass


@sessions_blueprint.route('/', methods=["GET"])
def index():
    return "INDEX-sessions.VIEW.py"


@sessions_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@sessions_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass

@sessions_blueprint.route('/logout')
def logout():
    logout_user()
    flash('Thank you for visiting. You are now logged out.', 'info')
    return redirect(url_for('home'))