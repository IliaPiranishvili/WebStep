from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from ext import db, login_manager


class Product(db.Model):

    __tablename__ = "products"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    dsc = db.Column(db.String(), nullable=False)
    img = db.Column(db.String(), nullable=True, default="default.jpg")


class Reg(db.Model, UserMixin):

    __tablename__ = "register"

    id = db.Column(db.Integer(), primary_key=True)
    user = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    role = db.Column(db.String())

    def __init__(self,user, password="New_Password", role="Guest"):
        self.user=user
        self.password=generate_password_hash(password)
        self.role=role

    def check_password(self, password):
        return check_password_hash(self.password,password)



@login_manager.user_loader
def search_user(reg_id):
    return Reg.query.get(reg_id)

