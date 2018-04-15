from pyramid.view import view_config

@view_config(route_name='paper', renderer='../templates/paper.jinja2')
def paper(request):
    paper_id = request.matchdict['paper_id']
    return {'project': 'papersummarize', 'paper_id': paper_id}
