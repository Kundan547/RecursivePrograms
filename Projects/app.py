from flask import Flask, jsonify

app = Flask(__name__)

# Sample data for books
books = [
    {"id": 1, "title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling"},
    {"id": 2, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
]

# Route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Route to get a specific book by its ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
