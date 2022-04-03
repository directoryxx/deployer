from werkzeug.wrappers import Request,Response
from app.models import WhiteList

class Middleware:

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)
        getIP = WhiteList.query.filter_by(ip=request.remote_addr,allowed='1').first()
        # Block if ip didnt in whitelist
        if getIP is None:
            res = Response(u'Not Found', mimetype= 'text/plain', status=404)
            return res(environ, start_response)

        return self.app(environ, start_response)