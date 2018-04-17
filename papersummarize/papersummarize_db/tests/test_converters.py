import unittest

import os
import pickle

from papersummarize_db.converters import ArxivConverter


cdir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(cdir, 'resources', 'db.p')


class ConverterTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_convert_one(self):
        db = pickle.load(open(db_path, 'rb'))
        one = db['1804.04647']
        paper = ArxivConverter.convert_one(one)

        self.assertEquals(paper.sid, '1804.04647')
        self.assertEquals(paper.source, 'arxiv')
        self.assertEquals(paper.link, 'http://arxiv.org/abs/1804.04647v1')
        self.assertEquals(paper.title, 'An efficient CNN for spectral reconstruction from RGB images')
        self.assertEquals(len(paper.authors), 2)
        self.assertEquals(paper.authors[0], 'Yigit Baran Can')
        self.assertEquals(paper.authors[1], 'Radu Timofte')


if __name__ == '__main__':
    unittest.main()
