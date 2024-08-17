from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S  ")
    return render_template('index.html', name = current_time)

@app.route("/blog/")
def blog():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S  ")
    return render_template('blog.html', name = current_time)

@app.route("/contacts/")
def contacts():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S  ")
    return render_template('contacts.html', name = current_time)
@app.route("/new/")
def new():
    return "new page"

if __name__ == '__main__':
    app.run(debug=True)