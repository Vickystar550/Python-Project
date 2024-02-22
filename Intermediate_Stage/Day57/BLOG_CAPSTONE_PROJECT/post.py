import requests


class Post:
    def __init__(self):
        self.blogs = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391').json()

    def retrieve_blog(self, id_):
        title_ = self.blogs[id_ - 1].get('title')
        subtitle_ = self.blogs[id_ - 1].get('subtitle')
        body_ = self.blogs[id_ - 1].get('body')
        return title_, subtitle_, body_
