from flask import Blueprint, render_template,request,url_for,redirect,flash
from werkzeug.security import generate_password_hash,check_password_hash
from models.image import Image
from models.user import User
from models.comment import Comment
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
        flash("Please select a file to upload", "warning")
        return redirect(url_for('images.new'))

    file    = request.files["user_file"]

    comment = request.form.get('comment')

    if file.filename == "":
        flash("Please select a file to upload", "warning")
        return redirect(url_for('images.new'))

    if file and allowed_file(file.filename):
        i = Image(user = current_user.id,img_name = file.filename)
        i.save()
        
        c = Comment(comment = comment, image = i.id, user = current_user.id)
        c.save()

        output   	  = upload_file_to_s3(file)
        flash("Image uploaded successfully", 'info')
        return redirect(url_for('users.show',username = current_user.username))

    else:
        flash("Sorry, we were unable to upload your photo. Please try again.", "warning")
        return redirect(url_for('images.new'))


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

    if "profile_image" not in request.files:
        flash("Please select a file to upload", "warning")
        return redirect(url_for('users.show', username=current_user.username))

    file    = request.files["profile_image"]

    if file.filename == "":
        flash("Please select a file to upload", "warning")
        return redirect(url_for('users.show', username=current_user.username))

    if file and allowed_file(file.filename):
        user = User.update(photo=file.filename).where(User.id==id)
        user.execute()
        output   	  = upload_file_to_s3(file)
        flash("Image uploaded successfully", 'success')
        return redirect(url_for('users.show', username=current_user.username))

    else:
        flash("Sorry, we were unable to upload your photo. Please try again.", "warning")
        return redirect(url_for('users.show', username=current_user.username))


@images_blueprint.route('delete/<id>', methods=['POST'])
def delete(id):
    image = Image.get_by_id(id)
    image.delete_instance(recursive=True)
    return redirect(url_for('users.show', username=current_user.username))
    


