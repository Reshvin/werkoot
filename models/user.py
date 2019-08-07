from models.base_model import BaseModel
import peewee as pw
from playhouse.hybrid import hybrid_property


class User(BaseModel):
    first_name = pw.CharField()
    last_name = pw.CharField()
    email = pw.CharField(unique=True)
    password = pw.CharField()
    username = pw.CharField(unique=True)
    photo = pw.CharField(null=True)

    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True

    def is_follow(self,user):
        for idol in self.idols:
            if idol.idol_id == user:
                return True

    @hybrid_property
    def profile_image_url(self):
        from werkoot_web.util.helpers import S3_LOCATION
        if self.photo:
            return S3_LOCATION + self.photo
        return 'https://www.biiainsurance.com/wp-content/uploads/2015/05/no-image.jpg'