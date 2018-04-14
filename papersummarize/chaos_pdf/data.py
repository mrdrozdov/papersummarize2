from reportlab.pdfgen import canvas


def hello():
    return 'hello chaos_pdf'


class PDFPage(object):
    def __init__(self, data):
        self.data = data

    def lines(self):
        return self.data.split('\n')


class PDFCreator(object):

    stroke_color = [0, 0, 0]
    fill_color = [0, 0, 0]
    font_family = 'Helvetica'
    font_size = 12
    font_point = 1
    inch = 72
    page_width = 8.5
    page_height = 11
    vertical_offset = 10
    vertical_space = 12

    def __init__(self, **kwargs):
        super(PDFCreator, self).__init__()
        for k, v in kwargs.items():
            self.setattr(k, v)


    def __type_check(self, pages):
        for p in pages:
            assert type(p) == PDFPage

    def write(self, path, pages):
        self.__type_check(pages)

        pagesize = (self.page_width * self.inch, self.page_height * self.inch)

        c = canvas.Canvas(path, pagesize=pagesize)
        c.setStrokeColorRGB(*self.stroke_color)
        c.setFillColorRGB(*self.fill_color)
        c.setFont(self.font_family, self.font_size * self.font_point)

        for i, page in enumerate(pages):
            v = self.vertical_offset * self.inch

            for line in page.lines():
                c.drawString(1 * self.inch, v, line)
                v -= self.vertical_space * self.font_point
            c.showPage()

        c.save()


if __name__ == '__main__':
    creator = PDFCreator()
    pages = [PDFPage('First Line\nSecond Line'), PDFPage('Second Page')]
    creator.write('/tmp/example.pdf', pages)
