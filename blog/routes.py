# from datetime import datetime
from flask import render_template
from flask import current_app as app

from .models import Articles

@app.route('/')
def home():

    articles = Articles.query.order_by(Articles.date.desc()).limit(4).all()
    return render_template("index.html", articles=articles)
