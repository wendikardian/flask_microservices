from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_marshmallow import Marshmallow
app = Flask(__name__)

# Decorators in Python


# To activate debug mode set FLASK_DEBUG=1


# @app.route('/')
# @app.route('/home')

# def hello_world():
#     # return '<h1>hello, World ! :) 123 123</h1>'
#     return render_template('home.html')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
app.app_context().push()

class Articles(db.Model):
    id = db.Column(db.Integer, primary_key  = True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text())
    date = db.Column(db.DateTime, default=datetime.datetime.now() )

    def __init__(self, title, body):
        self.title = title
        self.body = body



class ArticleSchema(ma.Schema):
    class Meta:
        field = ('id', 'title', 'body', 'date')

article_schema =  ArticleSchema()
articles_schema =  ArticleSchema(many = True)



@app.route('/get', methods = ['GET'])
def get_articles():
    return jsonify({"Hello" : "World"})

@app.route('/add', methods = ['POST'])
def add_article():
    title = request.json['title']
    body = request.json['body']


if __name__ == "__main__":
    app.run(debug=True)


