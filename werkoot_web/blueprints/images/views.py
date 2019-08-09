from flask import Blueprint, render_template,request,url_for,redirect,flash
from werkzeug.security import generate_password_hash,check_password_hash
from models.image import Image
from models.user import User
from flask_login import current_user
from werkoot_web.util.helpers import allowed_file,upload_file_to_s3

images_blueprint = Blueprint('images',
                            __name__,
                            template_folder='templates')


@images_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('images/new.html')


@images_blueprint.route('/', methods=['POST'])
def create():
    if "user_file" not in request.files:
        return "No user_file key in request.files"

    file    = request.files["user_file"]

    comment = request.form.get('comment')

    if file.filename == "":
        return "Please select a file"

    if file and allowed_file(file.filename):
        i = Image(user = current_user.id,img_name = file.filename)
        i.save()
        
        c = Comment(comment = comment, image = i.id, user = current_user.id)
        c.save()

        output   	  = upload_file_to_s3(file)
        return redirect(url_for('users.show',username = current_user.username))

    else:
        return redirect(url_for('images.new', id=id))


@images_blueprint.route('/<username>', methods=["GET"])
def show(username):
    pass

    
@images_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@images_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass

@images_blueprint.route('/display/<id>')
def display_img(id):
    image = Image.get_by_id(id)
    return render_template('images/img_display.html', image = image)


        
@images_blueprint.route('/<id>/images', methods=['POST'])
def upload_file(id):

    if "user_file" not in request.files:
        return "No user_file key in request.files"

    file    = request.files["user_file"]

    if file.filename == "":
        return "Please select a file"

    if file and allowed_file(file.filename):
        user = User.update(photo=file.filename).where(User.id==id)
        user.execute()
        output   	  = upload_file_to_s3(file)
        return str(output)

    else:
        return redirect(url_for('users.edit', id=id))
    


