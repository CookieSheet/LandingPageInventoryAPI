import os
from sqlite3 import SQLITE_ALTER_TABLE

basedir = os.path.abspath(os.path.dirname(__file__))

# Give access to the project in any OS we find ourselves in
# Allow outside files/folders to be added to the project from 
# base directory

class Config():
    """
    Set Config variables for flask app.
    Using Environment variables where available otherwise
    create the config variable if not done already
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or "Its a secret."
    SQLALCHEMY_DATABASE_URI= os.environ.get("DATABASE_URL") or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MOIFICATIONS = False