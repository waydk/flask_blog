# from datetime import datetime
from flask import render_template
from flask import current_app as app

from blog.admin_views import AuthException

from .models import Articles

@app.route('/')
def home():
    articles = Articles.query.order_by(Articles.date.desc()).limit(4).all()
    return render_template("index.html", articles=articles)

@app.route('/logout')
def Logout():
    raise AuthException('Successfully logged out.')
