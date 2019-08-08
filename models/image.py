from models.base_model import BaseModel
from models.user import User
import peewee as pw
from playhouse.hybrid import hybrid_property


class Image(BaseModel):
    img_name = pw.CharField()
    user = pw.ForeignKeyField(User,backref = 'images')

    @hybrid_property
    def image_url(self):
        from werkoot_web.util.helpers import S3_LOCATION
        return S3_LOCATION + self.img_name