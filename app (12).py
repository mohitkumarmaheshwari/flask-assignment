#9. Create a RESTful API using Flask to perform CRUD operations on resources like books or movies.from flask import Flask, render_template
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'  # SQLite database file
db = SQLAlchemy(app)
api = Api(app)

# Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

# Create the tables before the first request
with app.app_context():
    db.create_all()

# RESTful API resource for single book
class BookResource(Resource):
    def get(self, book_id):
        book = Book.query.get_or_404(book_id)
        return {'id': book.id, 'title': book.title, 'author': book.author}

    def put(self, book_id):
        data = request.get_json()
        book = Book.query.get_or_404(book_id)
        book.title = data['title']
        book.author = data['author']
        db.session.commit()
        return {'message': 'Book updated successfully'}

    def delete(self, book_id):
        book = Book.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
        return {'message': 'Book deleted successfully'}


# RESTful API resource for book collection
class BookListResource(Resource):
    def get(self):
        books = Book.query.all()
        return [{'id': book.id, 'title': book.title, 'author': book.author} for book in books]

    def post(self):
        data = request.get_json()
        new_book = Book(title=data['title'], author=data['author'])
        db.session.add(new_book)
        db.session.commit()
        return {'message': 'Book created successfully', 'id': new_book.id}


api.add_resource(BookResource, '/api/books/<int:book_id>')
api.add_resource(BookListResource, '/api/books')

# HTML routes for rendering web interface
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books')
def books():
    return render_template('books.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=5005)
