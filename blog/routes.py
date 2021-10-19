from environs import Env
from flask import render_template, request
from flask import current_app as app
import smtplib

from blog.admin_views import AuthException

from .models import Articles

env = Env()
env.read_env()

OWN_EMAIL = env('OWN_EMAIL')
OWN_PASSWORD = env('OWN_PASSWORD')

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


@app.route('/')
def home():
    articles = Articles.query.order_by(Articles.date.desc()).limit(4).all()
    return render_template("index.html", articles=articles)

@app.route('/logout')
def logout():
    raise AuthException('Successfully logged out.')

@app.route('/articles')
def show_articles():
    articles = Articles.query.order_by(Articles.date.desc()).all()
    return render_template('all_articles.html', articles=articles)

@app.route('/article/<title>')
def show_article(title):
    article = Articles.query.filter_by(title=title).first()
    return render_template('article.html', article=article)

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        try:
            send_email(data["name"], data["email"], data["phone"], data["message"])
        except UnicodeEncodeError:
            return render_template('contact.html', title='Your email was not sent (english only)')
        return render_template('contact.html', title='Your email has been sent')
    return render_template('contact.html', title='Contact me')
