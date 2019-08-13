from app import app
from flask import render_template
from werkoot_web.blueprints.users.views import users_blueprint
from werkoot_web.blueprints.sessions.views import sessions_blueprint
from werkoot_web.blueprints.measurements.views import measurements_blueprint
from werkoot_web.blueprints.images.views import images_blueprint
from werkoot_web.blueprints.fan_idol.views import fan_idol_blueprint
from werkoot_web.blueprints.comments.views import comments_blueprint
from flask_assets import Environment, Bundle
from .util.assets import bundles
from flask_wtf.csrf import CSRFProtect
from flask_login import current_user
from models.user import User
from models.image import Image
from models.fan_idol import FanIdol

csrf = CSRFProtect()
csrf.init_app(app)

assets = Environment(app)
assets.register(bundles)

app.register_blueprint(users_blueprint, url_prefix="/users")
app.register_blueprint(sessions_blueprint,url_prefix="/sessions")
app.register_blueprint(images_blueprint,url_prefix="/images")
app.register_blueprint(measurements_blueprint, url_prefix="/measurements")
app.register_blueprint(fan_idol_blueprint,url_prefix="/fan_idol")
app.register_blueprint(comments_blueprint,url_prefix='/comments')

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route("/")
def home():
    if current_user.is_authenticated:
        
        followers = User.select().join(FanIdol, on=(FanIdol.idol_id == User.id)).where((FanIdol.fan_id == current_user.id))

        images = Image.select().where((Image.user.in_(followers)) | (Image.user_id == current_user.id)).order_by(Image.created_at.desc())
    
        users = User.select()
        return render_template('images/index.html', images=images, users=users)
    else:
        return render_template('home.html')
