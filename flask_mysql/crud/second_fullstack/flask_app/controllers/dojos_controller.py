from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.dojos import Dojo
#from ..models.dog import User

@app.route("/dojos")
def index():
    return render_template("read_all2.html", all_dojos = Dojo.get_all())

@app.route("/dojos/create", methods = ['POST'])
def create_dojo():
    # print(request.form)
    Dojo.create(request.form)

    return redirect("/dojos")

@app.route('/dojos/<int:dojo_id>')
def display_user(dojo_id):
    return render_template("display.html", dojo = Dojo.get_one({"id": dojo_id}))




