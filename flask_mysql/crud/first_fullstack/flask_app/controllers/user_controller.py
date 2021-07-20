from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.user import User
#from ..models.dog import User

@app.route("/")
def index():
    return render_template("read_all.html", all_users = User.get_all())

@app.route("/users/new")
def new_user():
    return render_template("create.html")

@app.route("/users/create", methods = ['POST'])
def create_user():
    # print(request.form)
    User.create(request.form)

    return redirect("/")


@app.route('/users/<int:user_id>')
def display_user(user_id):
    return render_template("usersread.html", user = User.get_one({"id": user_id}))

@app.route("/users/<int:user_id>/edit")
def edit_user_form(user_id):
    return render_template("usersedit.html", user = User.get_one({"id": user_id}))

# perform the action of updating a single dog
@app.route("/users/<int:user_id>/update", methods = ["POST"])
def update_user(user_id):
    new_dict = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "id": user_id
    }
    User.update(new_dict)

    return redirect("/")

# perform the action of deleting a single dog
@app.route("/users/<int:user_id>/delete")
def delete_user(user_id):
    User.delete({"id": user_id})

    return redirect("/")



