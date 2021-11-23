from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Articles(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title_ru = db.Column(db.Text)
    title_en = db.Column(db.Text)
    content_ru = db.Column(db.Text)
    content_en = db.Column(db.Text)
    date = db.Column(db.DateTime)

    def __init__(self, title, content, date):
        self.title = title
        self.content = content
        self.date = date

    def __repr__(self):
        return "<Articles(title='%s', content='%s', date='%s')>" % (
            self.title, self.content, self.date)
