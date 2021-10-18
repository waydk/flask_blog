from blog import create_app, admin
from blog.models import Articles, db
from blog.admin_views import ArticleView

app = create_app()


if __name__ == '__main__':
	admin.add_view(ArticleView(Articles, db.session))
	app.run(debug=True)
