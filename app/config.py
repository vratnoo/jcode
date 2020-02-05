import os
basedir= os.path.abspath(os.path.dirname(__file__))
class Config(object):
	"""docstring for config"""

	
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
 	'sqlite:///' + os.path.join(basedir, 'app.db')


	SECRET_KEY=os.environ.get('SECRET_KEY') or "KRICODE"
	POSTS_PER_PAGE = 4