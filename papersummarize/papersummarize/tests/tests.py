import unittest

from pyramid import testing

from papersummarize.views.home import home
from papersummarize.views.paper import paper
from papersummarize_db.db import PSMongoDatabase


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.request = testing.DummyRequest()

        db_name = 'ps_demo_database'
        mongo_url = 'mongodb://0.0.0.0:27017'
        self.request.registry.db = PSMongoDatabase(db_name=db_name, mongo_url=mongo_url)

    def tearDown(self):
        testing.tearDown()

    def test_home_view(self):
        info = home(self.request)
        self.assertEqual(info['project'], 'papersummarize')

    def test_papers_in_feed(self):
        info = home(self.request)
        self.assertEqual(len(info['papers']), 30)

    def test_paper_id_in_url(self):
        paper_id = 'my-paper-id'
        self.request.matchdict['paper_id'] = paper_id
        info = paper(self.request)
        self.assertEqual(info['paper_id'], paper_id)


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from papersummarize import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'Paper Summarize' in res.body)

    def test_paper(self):
        paper_id = 'my-paper-id'
        paper_id_bytes = str.encode(paper_id)
        res = self.testapp.get('/p/{}'.format(paper_id), status=200)
        self.assertTrue(paper_id_bytes in res.body)


if __name__ == '__main__':
    unittest.main()
