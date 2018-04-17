from pyramid.view import view_config


@view_config(route_name='home', renderer='../templates/home.jinja2')
def home(request):
    page = int(request.params.get('page', 0))
    limit = 30
    start = page * limit
    end = (page+1) * limit
    papers = request.registry.db.find()[start:end]
    return {'project': 'papersummarize', 'papers': papers}
