"""Start point for Eucalypto web server"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")


@app.route('/login/')
def login_page():
    return render_template("login.html")

@app.route('/species/')
def species_page():
    return render_template("species_list.html")

@app.route("/spaces/")
def spaces_page():
    return render_template("spaces.html")


if __name__ == "__main__":
    app.run(debug=True)