from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_heroku import Heroku

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI']=''

heroku = Heroku(app)
db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__='books'
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(120))
    author=db.Column(db.String)

    def __init__(self,title,author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Title {self.title}" 

@app.route("/")
def home():
    return"<h2>Python CRUD Apis<h2>"

@app.route('/book/input', methods=['POST'])
def books_input():
    if request.content_type == 'application/json':
        post_data = request.get_json()
        title = post_data.get('title')
        author = post_data.get('author')
        reg = Book(title, author)
        db.session.add(reg)
        db.session.commit()
        return jsonify('Data Posted')
    return jsonify('Something went wrong')    

app.run()         