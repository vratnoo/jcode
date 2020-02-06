from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flaskext.markdown import Markdown


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
Markdown(app)
Migrate = Migrate(app,db,compare_type=True)
bootstrap = Bootstrap(app)
from app import routes
