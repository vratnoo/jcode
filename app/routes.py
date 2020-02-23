from app import app
from flask import render_template,request,redirect,flash,url_for
from app.model import Post,Tag,Page
from werkzeug.utils import secure_filename
from flask_uploads import UploadSet,configure_uploads
import json,os
from helper import is_active

# contaxt process
@app.context_processor
def helper_processor():
	pages = Page.query.all()
	tags = Tag.query.all()
	return dict(is_active=is_active,pages=pages,tags=tags)





@app.route('/')
def index():
	app.config['CU_PAGE'] = "index"

	posts = Post.query.all()
	
	return render_template('index.html',title="Jeeblog",posts=posts)


@app.route('/post/<post_name>')
def post(post_name):
	
	posts = Post.query.filter_by(title=post_name)
	p = Post.query.filter_by(title=post_name).first()
	print(posts)
	app.config['CU_PAGE'] = "post"
	
	return render_template('article.html',title="JEEBLOG",posts=posts,)
@app.route('/tags/<tag>')
def tags(tag):
	pages  = Page.query.all()
	p = Tag.query.filter_by(name=tag).first()
	tags = Tag.query.all()
	posts  = p.posts.all()
	return render_template('index.html',title="Jeeblog",posts=posts)

@app.route('/page/<page>')
def page(page):
	print(request.url)
	app.config['CU_PAGE'] = page
	pages  = Page.query.all()
	p = Page.query.filter_by(name=page).first()
	print(p)
	return render_template('index.html',title="Jeeblog",posts=p.posts)
# photo uploads functionnulity
@app.route('/photo', methods=['GET', 'POST'])
def photo():
	if request.method == 'POST':
		if 'file' not in request.files:
			flash("Thera is not any file")
			redirect(url_for('photo'))
		if request.files == '':
			flash('Please select file')
			redirect(url_for('photo'))
		file = request.files['file']
		
		allowed_file = file.filename.rsplit('.')[1].lower() in app.config['ALLOWED_EXTENSIONS']
		if allowed_file:
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
			redirect(url_for('photo'))
		
	return render_template('photo.html',title="jeeblog")

# wraper of file uploading
@app.route('/upload', methods=['GET', 'POST'])
def upload():
	photos = UploadSet('photos')
	configure_uploads(app, photos)
	if request.method == 'POST' and 'file' in request.files:
		filename = photos.save(request.files['file'])
		# rec = Photo(filename=filename, user=g.user.id)
		# rec.store()
		flash("Photo saved.")
		return redirect(url_for('upload'))
	return render_template('photo.html')