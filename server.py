from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', across = 8, down = 8)

@app.route('/<num>')
def callDown(num):
    return render_template('index.html', across = 8, down = int(num))


if __name__=="__main__":
    app.run(debug=True)