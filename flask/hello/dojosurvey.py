from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe."
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("dojosurvey.html")

@app.route('/process', methods=['POST'])
def submit_form():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['favlang'] = request.form ['favlang']
    session['comment'] = request.form['comment']
    return redirect('/result')
#     # Never render a template on a POST request.``
#     # Instead we will redirect to our index route.
#     return redirect('/show')  

@app.route("/result")
def redirect_result():
    print(session['name'])
    return render_template("dojosurvey2.html",
        name = session['name'],
        location = session['location'],
        favlang = session['favlang'],
        comment = session['comment']
        )




if __name__ == "__main__":
    app.run(debug=True)
