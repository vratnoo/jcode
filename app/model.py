import json
from app import db
from datetime import datetime
# class Post():
    
#     def post_data(tags):
#         with open("page_data.json",'r+') as file :
#             posts = json.load(file)
#         if tags :
#             p = []
#             for i in posts:
#                 print(i["tag"])
#                 if i["tag"] == tags :
#                     p.append(i)
#             posts = p
#         return posts
tag_post = db.Table('tag_post',db.Column('post_id',db.Integer,db.ForeignKey('post.id')),
                                db.Column('tag_id',db.Integer,db.ForeignKey('tag.id')))

class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50))
    body=db.Column(db.Text)
    timestamp=db.Column(db.DateTime,index=True,default=datetime.utcnow)
    #user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    page_id = db.Column(db.Integer,db.ForeignKey('page.id'))
    page = db.relationship('Page',backref='posts',lazy=True)
    tags = db.relationship('Tag',secondary='tag_post',backref=db.backref('posts',lazy='dynamic'))


    def __repr__(self):
        return '<post body {} user'.format(self.body)


# class for tag systemm
class Tag(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))

    def __repr__(self):
        return f"Tag is {self.name}"


class Page(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))
    


