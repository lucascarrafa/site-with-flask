from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')

manager = Manager(app)

from app.controllers import default

