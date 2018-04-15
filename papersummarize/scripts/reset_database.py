import argparse
from papersummarize_db.db import PSMongoDatabase, Paper
import time


def reset_database(options):
    db_name = options.db_name
    mongo_url = options.mongo_url

    db = PSMongoDatabase(db_name, mongo_url)

    Paper.drop_collection()

    documents = [
        Paper(author='Stephen Hawking', title='The Classics (aka Physics) and Music'),
        Paper(author='Michael', title='"Whoop! There is gradients", and other hits')
    ]

    results = db.batch_add(documents)

    print('collection has {} documents'.format(len(db.find())))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--db_name', type=str, default='ps_demo_database')
    parser.add_argument('--mongo_url', type=str, default='mongodb://0.0.0.0:27017')
    options = parser.parse_args()

    reset_database(options)
