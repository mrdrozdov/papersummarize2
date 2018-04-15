from pyramid.config import Configurator

# Mongo
from urllib.parse import urlparse
from gridfs import GridFS
from pymongo import MongoClient

from papersummarize_db.db import PSMongoDatabase


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)

    db_name = 'ps_demo_database'
    mongo_url = 'mongodb://0.0.0.0:27017'
    config.registry.db = PSMongoDatabase(db_name=db_name, mongo_url=mongo_url)

    config.add_route('home', '/')
    config.add_route('paper', '/p/{paper_id}')
    config.scan()
    return config.make_wsgi_app()
