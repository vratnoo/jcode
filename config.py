import os
basedir= os.path.abspath(os.path.dirname(__file__))
class Config(object):
	"""docstring for config"""

	
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
 	'sqlite:///' + os.path.join(basedir, 'app.db')
# file upload contraint
	UPLOAD_FOLDER = os.path.join(basedir,'uploads')
	UPLOADED_PHOTOS_DEST = UPLOAD_FOLDER 
	
	ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
	UPLOADED_PHOTOS_ALLOW= ALLOWED_EXTENSIONS
	SECRET_KEY=os.environ.get('SECRET_KEY') or "KRICODE"
	POSTS_PER_PAGE = 2
	CU_PAGE = ""