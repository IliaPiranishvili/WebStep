from models import Product, Reg
from ext import app, db
from flask_login import LoginManager


with app.app_context():
    db.drop_all()
    db.create_all()



    admin = Reg(user="Admin", password="Ilia123.", role="Admin")

    db.session.add(admin)
    db.session.commit()
