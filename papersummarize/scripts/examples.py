import argparse
from mongoengine import *

def run_mongo_demo(options):
    import datetime
    
    from urllib.parse import urlparse

    db_url = urlparse('mongodb://0.0.0.0:27017')
    connect('demo_database', host=db_url.hostname, port=db_url.port)

    class Post(Document):
        author = StringField(max_length=50)
        data = DictField()

    post = Post(author="Mike", data={
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
    })
    post.save()

    print('count={}'.format(len(Post.objects)))
    print(post.to_json())

    Post.drop_collection()

    print('count={}'.format(len(Post.objects)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('demo', choices=('mongo'))
    options = parser.parse_args()


    if options.demo == 'mongo':
        run_mongo_demo(options)
