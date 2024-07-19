"""Start point for Eucalypto web server"""

from flask import Flask
from flask import render_template, redirect
from flask import request, session, url_for

app = Flask(__name__)
app.secret_key = b'temporary_key' # TODO USE VAULT KEY FOR SIGNING

test_user = "user"
test_password = "password"

@app.route('/')
def home_page():
    return render_template("home.html")


@app.route('/login/', methods = ['GET', 'POST'])
def login_page():
    if request.method == 'GET':
        if session['logged_in']:
            return redirect(url_for('home_page'))
        else:
            return render_template("login.html")
    if request.method == 'POST':
        if request.form['username'] == "user" and request.form['password'] == "password":
            session['logged_in'] = True
            return redirect(url_for('home_page'))
        else:
            # Print user name/password error
            return render_template('login.html')
    

@app.route('/signout', methods = ['POST'])
def sign_out():
    session.pop('username', None)
    session['logged_in'] = False
    return redirect(url_for('home_page'))

@app.route('/species/')
def species_page():
    return render_template("species_list.html")

@app.route("/spaces/")
def spaces_page():
    return render_template("spaces.html")


if __name__ == "__main__":
    app.run(debug=True)