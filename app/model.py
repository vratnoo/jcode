import json
class Post():
    
    def post_data(tags):
        with open("page_data.json",'r+') as file :
            posts = json.load(file)
        if tags :
            p = []
            for i in posts:
                print(i["tag"])
                if i["tag"] == tags :
                    p.append(i)
            posts = p
        return posts
