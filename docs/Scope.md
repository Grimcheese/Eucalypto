# Project Scope and Outline

Eucalypto is a database of plants and observations of plants in a garden, or a 'space'. The database is accessible via a web server which users can log on to, create 'spaces' add plant information and add updates over time. Multiple users can access the same space and make changes as allowed by the space owner. Photos can also be uploaded of the plants to visually document changes over time.
### Plants
Plants are the core feature of the Eucalypto database.

The database should maintain a complete species list of all plants that have been added to the database as well as a list of actual plants that users have added to each space. Generic plants (in the species list) can be added by users if the species is not yet listed in the database. 

Generic plant information can include:
- family name
- genus
- species
- common names
- habit
- average dimensions
- leaf description
- flower description
- flowering times
- type photo

Actual plant information can include:
- Plant species
- Date planted
- Current dimensions
- Ongoing log of observations
- Current photo

Plant observations can include:
- Is the plant flowering?
- Growth status
- Are seeds present
- Any pests or diseases found
- New dimensions
- Any wildlife found 

### Spaces
Spaces are a core concept of Eucalypto that allows for having multiple places tracked and monitored. Essentially a space is a single, relatively small area that is grouped into one place. For example, a space could be your backyard while another space could be inside the house to track indoor plants. Spaces should have a name and a GPS coordinate. Spaces are only viewable by users that have been granted permission by the creator of that space, update permissions can also be granted.

Having separate spaces that users can manage makes the website far more usable and scalable without having to run multiple web sites for each place that a user (or group of users) would want to keep track of.

### Website
The website is the main way that the database will be interacted with. It will be the way that users add plants to the database, create new spaces and view plants from the database and spaces that they have access to. Pages need to be created that allow users to interact with the database in this way and pages for letting users log in and manage their accounts and spaces. 

The website will need to interact with the database system used. 

Pages to be created include:
- Home page (menus and list of recently added plants)
- Login page
- View spaces page
- Account management page
- Space overview page (location and list of plants)
- Generic plant page
- Actual plant page
- Add plant page
- Make observation page

The website will be created using Flask from the Python programming language as it is lightweight, configurable and works well with databases.
### Database
The database needs to store a list of generic plants and all the information that users upload about actual plants that exist in spaces. It will also be required to store user data and track user permissions for spaces. The information that needs to be stored in the database has been listed in the previous outlines and more thorough analysis will be conducted as part of development of the database.

But generally the entities existing in the database include:
- Generic plants
- Actual plants
- Observations
- Spaces
- Users
- Images

There may be a need for other entities such as pests or diseases but that will be determined when implementing the observations. 

Photos will be a core part of the web site and so need to be referenced in some way by the database. The images themselves can be stored on a mounted file system and the database can track the path and what that image actually refers to. A naming scheme will need to be decided for photos as they are uploaded to the system.

A relational database is perfect for this setup as it allows for storing and managing the complex relationships that exist between generic plants, actual plants, observations, spaces, and the users themselves. PostgreSQL will be used for Eucalypto as it is open source and freely accessible. 