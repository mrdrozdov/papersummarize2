from pyramid.view import view_config


def new_feed(request):
    papers = request.registry.db.find()
    return {'project': 'papersummarize', 'papers': papers}
