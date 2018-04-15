from urllib.parse import urlparse
from mongoengine import *

from papersummarize_db.paper import Paper


class PSDatabase(object):
    def __init__(self):
        super(PSDatabase, self).__init__()

    def find(self):
        raise NotImplementedError

    def batch_add(self, documents):
        raise NotImplementedError


class PSMongoDatabase(PSDatabase):
    def __init__(self, db_name, mongo_url):
        super(PSMongoDatabase, self).__init__()
        db_url = urlparse(mongo_url)
        print('connecting to mongo using name={} and url={}'.format(db_name, mongo_url))
        connect(db_name, host=db_url.hostname, port=db_url.port)

    def find(self):
        return Paper.objects

    def batch_add(self, documents):
        return list(map(lambda x: x.save(), documents))


class PSFakeDatabase(PSDatabase):
    def find(self):
        return [
            dict(author='Stephen Hawking', title='The Classics (aka Physics) and Music'),
            dict(author='Michael', title='"Whoop! There is gradients", and other hits')
        ]
