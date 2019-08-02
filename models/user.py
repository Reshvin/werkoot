from models.base_model import BaseModel
import peewee as pw


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
