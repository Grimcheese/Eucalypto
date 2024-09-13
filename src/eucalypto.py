"""Start point for Eucalypto web server"""

from flask import Flask
from flask import render_template, redirect
from flask import request, session, url_for
from flask import g

import db
from read_config import Config

app = Flask(__name__)
app.secret_key = b'temporary_key' # TODO USE VAULT KEY FOR SIGNING

test_user = "user"
test_password = "password"

config = Config()

@app.route('/')
def home_page():
    session['logged_in'] = False
    return render_template("home.html")


@app.route('/login/', methods = ['GET', 'POST'])
def login_page():
    if request.method == 'GET':
        if session['logged_in']:
            return redirect(url_for('home_page'))
        else:
            return render_template("login.html", login_error=False)
    if request.method == 'POST':
        if validate_user_login(request.form['username'], request.form['password']):
            session['logged_in'] = True
            return redirect(url_for('home_page'))
        else:
            # Print user name/password error
            return render_template('login.html', login_error=True)
    

@app.route('/signout', methods = ['POST'])
def sign_out():
    session.pop('username', None)
    session['logged_in'] = False
    return redirect(url_for('home_page'))


@app.route('/species/')
def species_page():
    # TODO get species list
    return render_template("species_list.html")


@app.route('/species/<genus>/<species>')
def generic_plant(genus, species):
    # Very genus and species is in plant list

    # Get info from genus and species in database
    plant_info = {
        'valid' : False,
        'family' : "test_fam",
        'genus' : genus,
        'species' : species
    }
    return render_template("generic_plant_page.html", plant_info=plant_info)


@app.route("/spaces/")
def spaces_page():
    space_ids = [1,2] # Generate urls for each space then pass to template
    space_names = ["Space 1", "The second place"]
    spaces = {}
    for i in range(len(space_ids)):
        spaces[space_names[i]] = url_for('user_space', space_id=space_ids[i])

    return render_template("spaces.html", spaces=spaces)


@app.route('/signup')
def signup_page():
    return render_template("signup.html")


@app.route('/spaces/<space_id>')
def user_space(space_id):
    # TODO validate user is logged in and has read access to space
    if session["logged_in"] == True:
        # Get space data - name, location, plant list
        space_data = [
            "test_space",
            "123 Road Ave",
            ["Boronia", "Eucalyptus"]
        ]
        return render_template("base.html", space_data=space_data)
    else:
        return render_template("error.html", 
                               error_name="Cannot display space", 
                               error_message="For some reason you cannot view this space. Maybe you aren't logged in, don't have permission or the space does not exist.")


def validate_user_login(user, password):
    db = get_db()
    
    if user in db.get_users() and password == db.get_pwd(user):
        return True
    else:
        return False
    


def get_db():
    if 'db' not in g:
        g.db = db.db_connect(config)

    return g.db

@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)

    if db is not None:
        db.close()


if __name__ == "__main__":
    app.run(debug=True)