from flask import Blueprint, render_template,request,url_for,redirect,flash
from werkzeug.security import generate_password_hash,check_password_hash
from models.image import Image
from models.user import User
from models.comment import Comment
from flask_login import current_user
from werkoot_web.util.helpers import allowed_file,upload_file_to_s3

comments_blueprint = Blueprint('comments',
                            __name__,
                            template_folder='templates')


@comments_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('comments/new.html')


@comments_blueprint.route('/', methods=['POST'])
def create():

    comment = request.form.get('comment')
    image = request.form.get('image')

    c = Comment(comment = comment, image = image, user = current_user.id)

    c.save()

    return redirect(url_for('images.display_img',id = image))

@comments_blueprint.route('/<username>', methods=["GET"])
def delete(username):
    pass
    

    
@comments_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@comments_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass


        



