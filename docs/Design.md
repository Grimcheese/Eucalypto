# Project Design
The project can be split up into 3 main parts: the web server, the database, 
and the actual installation/implementation of the server on a machine (VM).

Once these three parts are completed the project will enter it's final phase
of running/maintenance. Future updates and major feature additions are possible 
but are beyond the scope of the initial planning for this project.

## Web Server Design
The web server will take up the bulk of development time as it has multiple 
parts that need to be designed, developed and implemented in conjunction with
the other aspects of the project. The web site needs to serve pages to users,
allow updates, deletions, allow users to view plant information, handle user 
sessions, and interact with the database. 

The main parts of this development section include:
- Database API for adding, updating and deleting plant info and user info
- Create end routes in web server using Flask (Python)
- Create HTML pages using jinja2 templates

Part of the web server development will include setting up workflows and actions
to allow for updating of the web site from updates to the git repository.

### Database API
The API needs to be able to manipulate user data as well as plant and spaces 
data.

User data:
- Add new users
- Query users for logging in
- Query user permissions for access to certain areas of site
- Allow users to manage their account information

Plant data:
- Add new species
- Add new spaces
- Add new plants in spaces
- Make observations on a plant in spaces
- View spaces and plants in spaces

### Flask Server
The Flask server needs to have endroutes set up to handle requests for each page
that a user might request from the server. The server also needs to pass 
data between the users and the database as required and restrict access based
on permissions of users. 

Authentication needs to be implemented to ensure users only access and modify 
data they are authorised to.

### HTML

The web pages need to be created include:
- Home Page
- Login Portal
- User account 
- Space
- New plant
- Species list
- Species view
- Actual plant view
- Make observation

The HTML pages will utilise jinja2 templates to ensure a consistent look across
the site. 

## Database Design
The main backend of Eucalypto is the database that stores all information for
the web server to function. This means that thorough planning is required to
ensure the database is up to the task.

### Phases
There are two main parts of the design process - analysis to determine what
the database should look like, and then the installation and setup of the 
database on the web server.

#### Analysis
- Overview of functional requirements to assess and identify what needs to be
stored within the database
- Create an ERD to map the entities, relationships between them and their
attributes
- Map the ERD to a schema
- Perform any final analysis on the schema before implementing in PostgreSQL

#### Implementation
- Download/Install PostgreSQL on web server
- Create DDL schema file from determined schema
- Create database
- Setup users and permissions for the database 

## Installation/Implementation
Once the database has been implemented and set up the web server can be run to
test functionality. 

Tasks:
- Install and setup PostgreSQL database
- Run webserver from repository
- Test functionality on local network
- Ensure security protocols in place (limit SSH access, fail2ban, setup SSL)
- Open server on the internet
- Test
- Update and patch as required
