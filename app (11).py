#9. Create a RESTful API using Flask to perform CRUD operations on resources like books or movies.
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Sample data: a list of dictionaries representing books
books = [
    {'id': 1, 'title': 'Book 1', 'author': 'Author 1'},
    {'id': 2, 'title': 'Book 2', 'author': 'Author 2'},
    {'id': 3, 'title': 'Book 3', 'author': 'Author 3'}
]


class BookResource(Resource):
    def get(self, book_id=None):
        if book_id:
            book = next((book for book in books if book['id'] == book_id), None)
            if book:
                return jsonify({'book': book})
            else:
                return jsonify({'message': 'Book not found'}), 404
        else:
            return jsonify({'books': books})

    def post(self):
        data = request.get_json()
        new_book = {
            'id': len(books) + 1,
            'title': data['title'],
            'author': data['author']
        }
        books.append(new_book)
        return jsonify({'message': 'Book added', 'book': new_book}), 201

    def put(self, book_id):
        data = request.get_json()
        book = next((book for book in books if book['id'] == book_id), None)
        if book:
            book.update(data)
            return jsonify({'message': 'Book updated', 'book': book})
        else:
            return jsonify({'message': 'Book not found'}), 404

    def delete(self, book_id):
        global books
        books = [book for book in books if book['id'] != book_id]
        return jsonify({'message': 'Book deleted'}), 200


api.add_resource(BookResource, '/books', '/books/<int:book_id>')

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=5005)
