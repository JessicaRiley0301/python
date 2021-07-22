from flask import render_template, redirect, request, session, flash

from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route("/dashboard")
def dashboard():
    if "uuid" not in session:
        return redirect("/")
    
    return render_template(
        "dashboard.html", 
        logged_in_user = User.get_by_id({"id": session['uuid']}),
        all_recipes = Recipe.get_all()
    )

@app.route("/recipe/new")
def new_recipe():
    if "uuid" not in session:
        return redirect("/")
#some wireframes expect you to dispaly the name of the logged in user on this page,then you would pass in
# the logged in user, other wireframes don't require it at all, just there to create a form so no need)
    return render_template("newrecipe.html", new_recipe = User.get_by_id({"id": session['uuid']}))

@app.route("/recipe/create", methods = ["POST"])
def create_recipe():
    print(request.form)

    if not Recipe.validate(request.form):
        return redirect("/recipe/new")
    
    post_data = {
        **request.form,
        "user_id": session['uuid']
    }
    Recipe.create(post_data)

    return redirect("/dashboard")

@app.route("/recipe/<int:id>")
def dispaly_recipe(id):
    if "uuid" not in session:
        return redirect("/")
    
    return render_template(
        "displayrecipe.html", 
        logged_in_user = User.get_by_id({"id": session['uuid']}),
        recipe = Recipe.get_one({"id": id})
    )


@app.route("/recipe/<int:id>/delete")
def delete_recipe(id):
    Recipe.delete({"id": id})

    return redirect('/dashboard')

@app.route("/recipe/<int:id>/edit")
def edit_recipe(id):
    if "uuid" not in session:
        return redirect("/")

    return render_template(
        "editrecipe.html", 
        logged_in_user = User.get_by_id({"id": session['uuid']}),
        recipe = Recipe.get_one({"id" : id})
    )

@app.route("/recipe/<int:id>/update", methods = ['POST'])
def update_recipe(id):
    if not Recipe.validate(request.form):
        return redirect(f"/recipe/{id}/edit")

    post_data = {
        **request.form,
        "id": id
    }

    Recipe.update(post_data)

    return redirect("/dashboard")


