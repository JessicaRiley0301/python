from flask import Flask

app = Flask(__name__)
# import statements, maybe some other routes

@app.route("/")
def index():
    return "Hello World"

@app.route('/dojo')
def success():
    return "Dojo!"

@app.route('/say/<name>')
def hello(name):
    print(name)
    return f"Hi {name}!"

@app.route('/repeat/<int:num>/<something>')
def repeat(num, something):
    return f"{something}" * num



# localhost:5000/repeat/35/hello - have it say "hello" 35 times
# localhost:5000/repeat/80/bye - have it say "bye" 80 times
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times


if __name__ == "__main__":
    app.run(debug = True)

