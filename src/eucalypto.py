"""Start point for Eucalypto web server"""

from flask import Flask
from flask import render_template, redirect
from flask import request, session, url_for
from flask import g

import db
from read_config import Config
import psycopg2

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
    """Allow the user to login using a standard login form with username and password"""

    # Display login form to users or home page if already logged in
    if request.method == 'GET':
        if session['logged_in']:
            return redirect(url_for('home_page'))
        else:
            return render_template("login.html", login_error=False)

    # Submit user login details and attempt login
    try:    
        if request.method == 'POST':
            if validate_user_login(request.form['username'], request.form['password']):
                session['logged_in'] = True
                return redirect(url_for('home_page'))
            else:
                # Print user name/password error
                return render_template('login.html', login_error=True)
    except psycopg2.OperationalError as e:
        # Connecting to database failed
        print("Connecting to database failed")
        return render_template('error.html', 
            error_name="Login error",
            error_message="An error occurred logging in - contact administrator")


@app.route('/signout', methods = ['POST'])
def sign_out():
    session.pop('username', None)
    session['logged_in'] = False
    return redirect(url_for('home_page'))


@app.route('/species/')
def species_page():
    """Display the site species list."""
    
    try:
        plant_list = get_all_species()
        return render_template("species_list.html", plant_list=plant_list)
    except Exception:
        return render_template("error.html", 
            error_name="Database Error", 
            error_message="Error getting species list - contact administrator")
    

def get_all_species():
    """Get all the generic plants for use on species page.
    
    Returns: List of all plants named by genus and species stored
        as generic plants in the database.
    """

    db_connection = get_db()
    raw_plant_list = db.query(db_connection,
        "SELECT genus, species, image_id \
            FROM generic_plants AS gp, gp_images AS gpi \
                WHERE gp.g_plant_id=gpi.g_plant_id \
                    ORDER BY genus ASC, species ASC")

    # Create dictionary of genus species:image_id 
    plant_dictionary = {}
    for line in raw_plant_list:
        plant_dictionary[f"{line[0]} {line[1]}"] = line[2]

    return plant_dictionary


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

    # TODO Get spaces for the user
    space_ids = get_user_spaces()
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