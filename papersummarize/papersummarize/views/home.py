from pyramid.view import view_config

from .feed import new_feed


@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def home(request):
    return new_feed(request)
