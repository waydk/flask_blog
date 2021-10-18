from flask import Response
from flask_admin.contrib.sqla import ModelView
from werkzeug.exceptions import HTTPException
from . import basic_auth


# login failed handler
# https://computableverse.com/blog/flask-admin-using-basicauth
class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(message, Response(
            message, 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))

class ArticleView(ModelView):
    def is_accessible(self):
        if not basic_auth.authenticate():
            raise AuthException('Not authenticated. Refresh the page.')
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return basic_auth.challenge()
