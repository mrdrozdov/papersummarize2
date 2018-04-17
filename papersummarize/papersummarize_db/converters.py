from papersummarize_db.paper import Paper


class Converter(object):
    def __init__(self, db_path):
        super(Converter, self).__init__()
        self.db_path = db_path
    
    @staticmethod
    def convert_one(doc):
        raise NotImplementedError


class ArxivConverter(Converter):
    @staticmethod
    def convert_one(doc):
        sid = doc['_rawid']
        source = 'arxiv'
        authors = list(map(lambda x: x['name'], doc['authors']))
        title = doc['title']
        link = doc['link']
        data = doc

        paper = Paper(sid=sid, source=source, authors=authors, title=title, link=link, data=data)

        return paper
