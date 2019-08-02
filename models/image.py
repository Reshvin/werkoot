from models.base_model import BaseModel
from models.user import User
import peewee as pw


class Image(BaseModel):
    img_name = pw.CharField()
    user = pw.ForeignKeyField(User,backref = 'images')

