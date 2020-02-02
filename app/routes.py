from app import app
from flask import render_template
from app.model import Post
import json
@app.route('/')
def index():
	
	posts = Post.post_data("")
	return render_template('index.html',title="Jeeblog",posts=posts)
@app.route('/tags/<tag>')
def tags(tag):
	posts = Post.post_data(tag)
	return render_template('index.html',title="Jeeblog",posts=posts)
