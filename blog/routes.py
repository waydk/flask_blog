from flask import render_template
from flask import current_app as app

from .models import Articles, db

@app.route('/')
def home():
    return render_template("index.html")
