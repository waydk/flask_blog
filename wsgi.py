from flask_admin.base import Admin
from blog import create_app
from blog.models import Articles, AriclesView, db

app = create_app()

if __name__ == '__main__':
	admin = Admin(app, name='waydk blog', template_mode='bootstrap4')
	admin.add_view(AriclesView(Articles, db.session))
	app.run(debug=True)
