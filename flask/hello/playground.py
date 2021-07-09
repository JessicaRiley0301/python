from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/play/<int:x>')
@app.route('/play/<int:x>/<color>')
def repeat_color(x = 3, color = "aqua"):
    return render_template("index2.html", color = color, times = x)

if __name__=="__main__":
    app.run(debug=True)