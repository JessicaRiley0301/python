from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<int:y>')
@app.route('/<int:y>/<int:x>')
def repeat_color(x=8, y=8):
    return render_template('checkerboard.html', row = x, column = y)

if __name__=="__main__":
    app.run(debug=True)