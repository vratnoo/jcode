from app import app
from flask import render_template
from app.model import Post,Tag,Page
import json
@app.route('/')
def index():
	pages  = Page.query.all()
	posts = Post.query.all()
	return render_template('index.html',title="Jeeblog",posts=posts,pages=pages)

@app.route('/tags/<tag>')
def tags(tag):
	pages  = Page.query.all()
	p = Tag.query.filter_by(name=tag).first()
	posts  = p.posts.all()
	return render_template('index.html',title="Jeeblog",posts=posts,pages=pages)

@app.route('/page/<page>')
def page(page):
	pages  = Page.query.all()
	p = Page.query.filter_by(name=page).first()
	print(p)
	return render_template('index.html',title="Jeeblog",posts=p.posts,pages=pages)