#Blog
#Python 3.6 Application
##Developer
David Ngatia
##Description of the application
    This application allows writers to create and update their blogs and other users can read and comment on them.

##Behaviour driven development
    The application displays all posts on the home page in the order of the posted time

    One should receive an email when signing up,subscribing.

    For one to comment one has to be signed in

    When signed in one can create a blog

##Project setup instructions
    You can install this app by cloning the repository:git clone git@github.com:davidngatia/pitch.git 
    cd blog/ atom . for those using atom or code . for those using visual studio.
    Live link
    You can find the live site here : https://davidblogger.herokuapp.com/ 

##Known Bugs
    There are no known bugs so far,everything is working.

##Technologies Used.
This project was generated with:
    - Python 3.6
    -flaskframework
    - HTML
    - Bootstrap 4
    - Heroku
    - Postgresql
    -SQLAlchemy

## Setup and installations

#### Prerequisites
1. [Python3.6](https://www.python.org/downloads/)
2. [Postgres](https://www.postgresql.org/download/)
3. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
4. [Pip](https://pip.pypa.io/en/stable/installing/)

#### Clone the Repo and checkout into the project folder.
```bash
git clone git@github.com:davidngatia/Blog.git
```

#### Create and activate the virtual environment
```bash
python3.6 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY='<Secret_key>'
NAME='tutorial'
USER='<Username>'
PASSWORD='<password>'
HOST='localhost'
MODE='dev'
DEBUG=True
DISABLE_COLLECTSTATIC=1
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Create the Database
In a new terminal, open the postgresql shell with `psql`.
```bash
CREATE DATABASE tutorial;
```

#### Make and run migrations
```bash
python3.6 manage.py makemigrations && python3.6 manage.py migrate
```

#### Run the app
```bash
./start.sh
```

## Support and contact details
Contact [David Ngatia](machngatia@gmail.com) for further help/support

### License
MIT

Copyright (c)2018 **David Ngatia**