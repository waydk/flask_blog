from crypt import methods
from environs import Env
from flask import render_template, request, redirect, url_for
from flask import current_app as app
import smtplib

from blog.admin_views import AuthException

from .models import Articles
import requests
from bs4 import BeautifulSoup

env = Env()
env.read_env()

OWN_EMAIL = env('OWN_EMAIL')
OWN_PASSWORD = env('OWN_PASSWORD')

def send_email(name, email, phone, message):
    """Sending an email to your own email account
    """
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


@app.route('/', methods=['GET', 'POST'])
def home():
    """Route for the homepage
    """
    articles = Articles.query.order_by(Articles.date.desc()).limit(4).all()
    if request.method == 'POST':
        try:
            anime_title = request.form.get('anime-title')
            r = requests.get(f'https://www.kinopoisk.ru/index.php?kp_query={anime_title}')
            soup = BeautifulSoup(r.text, 'lxml')
            most_wanted = soup.find('div', class_='element most_wanted')
            data_id = most_wanted.find('div', class_='info').find('p', class_='name').find('a').get('data-id')
            return  render_template("index.html", articles=articles, kinopoisk_id=data_id)
        except Exception:
            return render_template("index.html", articles=articles, kinopoisk_id=None)
    return render_template("index.html", articles=articles, kinopoisk_id=None)


@app.route('/logout')
def logout():
    """Route to exit the admin panel

    Raises:
        AuthException
    """
    raise AuthException('Successfully logged out.')

@app.route('/articles')
def show_articles():
    """Route to show all articles
    """
    articles = Articles.query.order_by(Articles.date.desc()).all()
    return render_template('all_articles.html', articles=articles)

@app.route('/article/<title>')
def show_article(title):
    """Route for the article

    Args:
        title ([str]): Article title
    """
    article = Articles.query.filter_by(title_en=title).first()
    return render_template('article.html', article=article)
