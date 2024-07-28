# Authentication, Secrets, and that rabbit hole...

The main purpose of this project is to allow me to upload and maintain my own database of information
about my garden and the plants within it. For the most part it is a personal, home project that could
be put on the internet. It does have a database, but there isn't a great deal of sensitive information
that will go within it, except maybe for usernames and passwords. If someone, somehow got into this
database it probably wouldn't be the end of the world but generally speaking, letting people on the
internet access your computers is a bad idea.

With all that said, I still want to try and follow best practices, if only for my own personal education 
on the best methods for handling and storing sensitive information. The first issue I have encountered regarding
safety concerns and secrets is to do with the credentials used to access the database. At some point 
the web server has to access the database and to do so it requires a username and password. Storing it
in plain text with the code is obviously not the best method given that this project is in a publically
hosted github repository. Researching and assessing the various options has lead me down a rabbit hole 
ending up at Hashi Corp's Vault.

Vault is most likely overkill for this project and at the early stages of this project I don't really
have the infrastructure required setup to get it to work in a way that I like. The current method I have,
using approles role-id and secret-id has boiled down to using a configuration file storing that 
information... which is pretty much where I started. So now I have a few decisions to make regarding
how to proceed from here. 

## Vault
Vault is a program that is designed for the exact situation that I am: "how to securely provide secrets to
a program", with the caveat that it is more focused on larger systems with more users. 

## The outcome

Ultimately I have decided that getting the project up and working is the most important part but I still
don't want to totally forgo using best practices and hardening the server. So for now I think allowing different options is best. Upon startup of the web server, an argument can be passed that determines what kind of
authentication and security protocols should be used to connect to the database (and potentially other
options further down the track).

The options might look something like this:
`-db_auth ["default", "vault"]
 -conf_file "path/to/config/file"
 `

And they can be added as options to the program start or written to a configuration file.