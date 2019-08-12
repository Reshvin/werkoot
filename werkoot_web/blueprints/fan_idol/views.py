from flask import Blueprint, render_template,request,url_for,redirect,flash,session
from werkzeug.security import check_password_hash
from models.user import User
from flask_login import login_user,logout_user,current_user
from models.fan_idol import FanIdol

fan_idol_blueprint = Blueprint('fan_idol',
                            __name__,
                            template_folder='templates/fan_idol')


@fan_idol_blueprint.route('/follow/<id>', methods=['POST'])
def follow(id):
    fan_idol = FanIdol(fan_id = current_user.id, idol_id = id)
    fan_idol.save()
    user = User.get_by_id(id)
    flash('Thank you for following.', 'success')
    return redirect(url_for('users.show',username = user.username))

@fan_idol_blueprint.route('/unfollow/<id>', methods=['POST'])
def unfollow(id):
    unfollow_user = FanIdol.delete().where(FanIdol.fan_id == current_user.id and FanIdol.idol_id == id)
    unfollow_user.execute()
    user = User.get_by_id(id)
    flash(f'You are no longer following {user.username}.', 'danger')
    return redirect(url_for('users.show',username = user.username))


    