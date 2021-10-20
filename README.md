# My portfolio project
*A simple blog written in python, using flask as the backend, bootstrap as the frontend, and postgres as the database*

<img src="https://user-images.githubusercontent.com/77948380/136917444-15b689ea-18c0-4a40-a4b3-6ea68cfa01a2.png" alt="waydk blog" width=600px>

## How to add articles to the website
* Go to <code>http://127.0.0.1:5000/admin/</code>

* Enter login and password (in .env <code>BASIC_AUTH_USERNAME</code>, <code>BASIC_AUTH_PASSWORD</code>)

![image](https://user-images.githubusercontent.com/77948380/137711539-6c5bed9b-383c-455a-bbd6-10dd034d5355.png)

* Go to <code>http://127.0.0.1:5000/admin/articles/</code> and click create

![image](https://user-images.githubusercontent.com/77948380/137712234-51e7ba9f-9c7a-4d70-9e75-0eeed1994448.png)


## Development
### System dependencies
* Python 3.8.10
* Flask-SQLAlchemy 2.5.1
* environs 9.3.4
* Flask-Admin 1.5.8
* Flask-BasicAuth 0.2.0
* psycopg-binary 3.0.1

### Setup environment
* Rename .env.dist to <b>.env</b>
* Fill in your <b>data</b>
* <code>SECRET_KEY</code> is needed to secure sessions on the client side

* <code>PG_HOST</code> is responsible for where your database is located
* <code>PG_USER and PG_PASSWORD</code> are needed to access the database
* <code>DATABASE</code> database name
* <code>BASIC_AUTH_USERNAME and BASIC_AUTH_PASSWORD</code> - to access the admin panel

### Launch
* <code>git clone https://github.com/waydk/flask_blog</code>
* <code>cd flask_blog</code>
* If you don't have poetry <code>pip install poetry</code>
* Install dependencies: <code>poetry install</code>
* Create a virtual environment <code>poetry env use python3.8 *or your version* </code>
* Activate the virtual environment <code>poetry shell</code>
* Launching an application <code>python3 wsgi.py</code>
