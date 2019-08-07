from models.base_model import BaseModel
import peewee as pw
from models.user import User


class Measurement(BaseModel):
    bicep = pw.DecimalField()
    user = pw.ForeignKeyField(User, backref = 'measurments')