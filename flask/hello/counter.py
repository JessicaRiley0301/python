from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/')
def visits(): 
    if 'visits' not in session:
        session['visits'] = 0
    else: 
        session['visits'] = session['visits'] + 2
    return render_template("counter.html")

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
