from app import app
from flask import render_template,request,redirect,flash,url_for,send_from_directory
from app.model import Post,Tag,Page
from werkzeug.utils import secure_filename
from flask_uploads import UploadSet,configure_uploads
import json,os
from helper import is_active,pagination

# contaxt process
@app.context_processor
def helper_processor():
	pages = Page.query.all()
	tags = Tag.query.all()
	bc = request.path.split("/")
	print(request.path)

	return dict(is_active=is_active,pages=pages,tags=tags,bc=bc[1:])



@app.route('/uploads/<path:filename>')
def uploads(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename, as_attachment=True)

@app.route('/')
def index():
	app.config['CU_PAGE'] = "index"
	bc = request.path.split("/")
	print(app.config['UPLOAD_FOLDER'])
	pg = request.args.get('pg',1,type=int)
	# posts = Post.query.all()
	posts = Post.query.paginate(pg,app.config['POSTS_PER_PAGE'],False)
	print(posts.pages)
	pgnate = pagination(pg,posts.pages,posts.next_num,posts.prev_num)



	
	return render_template('index.html',title="Jeeblog",posts=posts.items,pgnate=pgnate)


@app.route('/post/<post_name>')
def post(post_name):
	print(request.path)
	post = Post.query.filter_by(title=post_name).first()
	print(post)
	app.config['CU_PAGE'] = "post"
	
	return render_template('article.html',title="JEEBLOG",post=post)
@app.route('/tags/<tag>')
def tags(tag):
	print(request.path)
	pages  = Page.query.all()
	tags = Tag.query.all()
	p = Tag.query.filter_by(name=tag).first()
	print(p)
	pg = request.args.get('pg',1,type=int)
	posts  = p.posts.paginate(pg,app.config['POSTS_PER_PAGE'],False)
	pgnate = pagination(pg,posts.pages,posts.next_num,posts.prev_num)
	if(len(posts.items)==0):
		return render_template('404.html',title="Jeeblog")
	return render_template('index.html',title="Jeeblog",posts=posts.items,pgnate=pgnate)

@app.route('/page/<page>')
def page(page):
	print(request.path.split("/"))
	app.config['CU_PAGE'] = page
	pages  = Page.query.all()
	pg = request.args.get('pg',1,type=int)
	p = Page.query.filter_by(name=page).first()
	print(p.posts)
	posts  = p.posts.paginate(pg,app.config['POSTS_PER_PAGE'],False)
	pgnate = pagination(pg,posts.pages,posts.next_num,posts.prev_num)
	if(len(posts.items)==0):
		return render_template('404.html',title="Jeeblog")
	return render_template('index.html',title="Jeeblog",posts=posts.items,pgnate=pgnate)



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