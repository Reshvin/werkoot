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
            flash('Username not available.', 'danger')
            return redirect(url_for('users.new'))
        elif user.email == email:
            flash('The provided email is already in use.','warning')
            return redirect(url_for('users.new'))

    if len(password) < 6:
        flash("Password length has to be more than 6", 'warning')
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
    users = User.select().order_by(User.username.asc())
    text = "All users"
    return render_template('users/users.html', users = users, text = text)


@users_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    if not current_user.is_authenticated:
        return redirect (url_for('sessions.new'))
    else:
        user = User.get_by_id(id)
        if current_user == user:
            return render_template('users/edit.html',user=user)
        else:
            return redirect (url_for('index'))

@users_blueprint.route('/search', methods=['POST'])
def search():
    text = request.form.get('search')
    if text == '':
        text = "All users"
        users = User.select().order_by(User.username.asc())
    else:
        search = '%' + text + '%'
        text = "Usernames containing: " + text
        users = User.select().where(User.username ** search)
    
    return render_template('users/users.html', users = users, text = text)

@users_blueprint.route('search/<category>', methods=['GET'])
def get_by_category(category):
    
    if category == 'power':
        users = User.select().where(User.power == True)
        text = "Power"
    elif category == "endurance":
        users = User.select().where(User.endurance == True)
        text = "Endurance"
    elif category == "calisthenics":
        users = User.select().where(User.calisthenics == True)
        text = "Calisthenics"
    elif category == "teamsports":
        users = User.select().where(User.teamsports == True)
        text = "Team Sports"

    return render_template('users/users.html', users = users, text = text)

@users_blueprint.route('/<id>', methods=['POST'])
def update(id):
    old_email = request.form.get('old_email')
    old_username = request.form.get('old_username')
    old_password = request.form.get('old_password')
    new_email = request.form.get('new_email')
    new_username = request.form.get('new_username')
    new_password = request.form.get('new_password')
    confirm_password = request.form.get('confirm_password')
    new_hashed_password = generate_password_hash(new_password)
    new_bio = request.form.get('bio')

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

    user = User.get_by_id(id)

    

    if user.username != old_username:
        flash('Username is not the same')
        return redirect(url_for('users.new'))
    elif user.email != old_email:
        flash('Email is not the same')
        return redirect(url_for('users.new'))
    elif new_password != confirm_password:
        flash('Passwords are not the same')
        return redirect(url_for('users.new'))
    if not check_password_hash(user.password, old_password):
        flash('Incorrect password')
        return redirect(url_for('users.new'))

    user.username = new_username
    user.email = new_email
    user.password = new_hashed_password
    user.bio = new_bio
    user.power = power
    user.endurance = endurance
    user.calisthenics = calisthenic
    user.teamsports = team_sport
    user.save()

    flash('Profile successfully updated')
    return redirect(url_for('users.show',username = current_user.username))


