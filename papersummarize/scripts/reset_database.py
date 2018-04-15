import time
import pickle
import argparse

from papersummarize_db.db import PSMongoDatabase, Paper
from papersummarize_db.converters import ArxivConverter
from papersummarize_db.tests.test_converters import db_path as arxiv_path


def reset_database(options):
    db_name = options.db_name
    mongo_url = options.mongo_url

    db = PSMongoDatabase(db_name, mongo_url)

    Paper.drop_collection()

    arxiv_papers = pickle.load(open(arxiv_path, 'rb'))
    documents = [ArxivConverter.convert_one(p) for p in arxiv_papers.values()]
    results = db.batch_add(documents)

    print('collection has {} documents'.format(len(db.find())))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--db_name', type=str, default='ps_demo_database')
    parser.add_argument('--mongo_url', type=str, default='mongodb://0.0.0.0:27017')
    options = parser.parse_args()

    reset_database(options)
