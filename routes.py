from flask import render_template, redirect, flash
from flask_login import login_user, logout_user, login_required

from registration import Register, Post
from login import Login
from ext import app, db
from models import Product, Reg

import os



@app.route("/")
def home():
    products = Product.query.all()

    return render_template("main.html", products=products)

@app.route("/delete_posts/<int:post_id>")
@login_required
def delete_post(post_id):
    posts = Product.query.get(post_id)
    db.session.delete(posts)
    db.session.commit()

    return redirect("/")



@app.route("/login", methods=["GET", "POST"])
def login():
    form1 = Login()
    if form1.validate_on_submit():
        user = Reg.query.filter(form1.username.data == Reg.user).first()
        if user and user.check_password(form1.password.data ):
            print(user.check_password(form1.password.data))
            if user:
                login_user(user)
                flash("თქვენ წარმატებით გაიარეთ ავტორიზაცია")
                return redirect ("/")



    return render_template("Login.html", form1=form1)


@app.route("/register", methods=["GET", "POST"])
def registration():
    form = Register()
    if form.validate_on_submit():
        users = Reg(user=form.user.data, password=form.password.data)

        db.session.add(users)
        db.session.commit()
        flash("თქვენ წარმათებით გაიარეთ რეგისტრაცია")
        return redirect("/login")

    return render_template("Register.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")

@app.route("/About")
def about():
    return render_template("About.html")

@app.route("/Post", methods=["GET", "POST"])
@login_required
def post():
    form2 = Post()
    if form2.validate_on_submit():
        posts = Product(name=form2.postname.data, dsc=form2.discribe.data )

        image = form2.img.data
        if image:
            directory = os.path.join("static", image.filename)
            image.save(directory)
            posts.img = image.filename
        else:
            posts.img = "default.jpg"



        db.session.add(posts)
        db.session.commit()
        flash("თქვენ წარმატებით გამოაქვეყნეთ პოსტი")
        return redirect("/")

    return render_template("Post.html", form2=form2 )


@app.route("/details/<int:product_id>")
def details(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template("detailed.html", product=product)