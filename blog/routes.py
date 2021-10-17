# from datetime import datetime
from flask import render_template
from flask import current_app as app

from .models import Articles, db

@app.route('/')
def home():
    # article = Articles(title='Example title', content='Some content', date=datetime.now())
    # db.session.add(article)
    # db.session.commit()

    articles = Articles.query.limit(4).all()
    return render_template("index.html", articles=articles)
