import unittest
import tempfile, shutil, os

from PyPDF2 import PdfFileWriter, PdfFileReader

from .data import *


class DataTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hello(self):
        self.assertEquals(hello(), 'hello chaos_pdf')


class PDFPageTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pages_1(self):
        page = PDFPage('a')
        self.assertEquals(len(page.lines()), 1)

    def test_pages_2(self):
        page = PDFPage('a\na')
        self.assertEquals(len(page.lines()), 2)


class PDFCreatorTests(unittest.TestCase):
    def setUp(self):
        self.creator = PDFCreator()

    def tearDown(self):
        pass

    def test_writes_file(self):
        pages = [PDFPage('a')]
        _, path = tempfile.mkstemp()
        self.creator.write(path, pages)
        self.assertTrue(os.path.exists(path))
        self.assertTrue(os.path.getsize(path) > 0)
        os.remove(path)

    def test_writes_pages_1(self):
        pages = [PDFPage('a')]
        _, path = tempfile.mkstemp()
        self.creator.write(path, pages)
        pdf_file = PdfFileReader(open(path, 'rb'))
        self.assertEquals(pdf_file.getNumPages(), 1)
        os.remove(path)

    def test_writes_pages_2(self):
        pages = [PDFPage('a'), PDFPage('a')]
        _, path = tempfile.mkstemp()
        self.creator.write(path, pages)
        pdf_file = PdfFileReader(open(path, 'rb'))
        self.assertEquals(pdf_file.getNumPages(), 2)
        os.remove(path)
