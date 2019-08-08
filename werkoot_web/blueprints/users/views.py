from flask import Blueprint, render_template,request,redirect,url_for,flash
from models.user import User
from flask_login import current_user,login_user
from werkzeug.security import generate_password_hash,check_password_hash


users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')


@users_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('users/new.html')


@users_blueprint.route('/', methods=['POST'])
def create():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    bio = request.form.get('bio')
    power = False
    endurance = False
    calisthenic = False
    team_sport = False

    if request.form.get('power'):
        power = True
    if request.form.get('endurance'):
        endurance = True
    if request.form.get('calisthenic'):
        calisthenic = True
    if request.form.get('team_sport'):
        team_sport = True
    

    hashed_password = generate_password_hash(password)

    u = User(first_name=first_name, last_name=last_name,email=email,username=username,password =hashed_password,power=power,endurance=endurance,calisthenics=calisthenic,teamsports=team_sport,bio = bio)

    users = User.select()
    for user in users:
        if user.username == username:
            flash('Username not available')
            return redirect(url_for('users.new'))
        elif user.email == email:
            flash('Email not available')
            return redirect(url_for('users.new'))

    if len(password) < 6:
        flash("Password length has to be more than 6")
        return redirect(url_for('users.new'))
        
    if u.save():
        login_user(u)
        return redirect(url_for('users.show',username = current_user.username))


@users_blueprint.route('/<username>', methods=["GET"])
def show(username):
    user = User.get(User.username == username)
    return render_template('users/show.html', user = user)


@users_blueprint.route('/', methods=["GET"])
def index():
    return "INDEX-USERS.VIEW.py"


# @users_blueprint.route('/<id>/edit', methods=['GET'])
# def edit(id):
#     if not current_user.is_authenticated:
#         return redirect (url_for('sessions.new'))
#     else:
#         user = User.get_by_id(id)
#         if current_user == user:
#             return render_template('users/edit.html',user=user)
#         else:
#             return redirect (url_for('index'))


@users_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass
