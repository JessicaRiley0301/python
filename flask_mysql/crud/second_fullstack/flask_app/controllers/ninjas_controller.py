from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja
#from ..models.dog import User

@app.route("/ninjas")
def new_user():
    return render_template("new_ninja.html", all_dojos= Dojo.get_all())

@app.route("/ninja/create", methods = ['POST'])
def create_ninjas():
    # print(request.form)
    Ninja.create(request.form)

    return redirect("/dojos")


@app.route('/dojos/<int:dojo_id>')
def display_ninjas(user_id):
    return render_template("display.html", ninja = Ninja.get_all())



