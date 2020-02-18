from flask import Flask,flash,request,redirect
from config import Config
from flask_uploads import UploadSet,configure_uploads
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flaskext.markdown import Markdown
import os
STATIC_DIR = os.path.abspath('../static')


app = Flask(__name__,static_url_path='/static')
app.config.from_object(Config)
print(Config.UPLOAD_FOLDER)

db = SQLAlchemy(app)
Markdown(app)
Migrate = Migrate(app,db,compare_type=True)
bootstrap = Bootstrap(app)
from app import routes
