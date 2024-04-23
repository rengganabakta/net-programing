from flask import Flask, jsonify, request

app = Flask(__name__)

# Data sementara untuk contoh
books = [
    {"id": 1, "title": "Python Programming", "author": "John Doe"},
    {"id": 2, "title": "Web Development with Flask", "author": "Jane Smith"}
]

# Endpoint untuk mendapatkan daftar semua buku
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({"books": books})

# Endpoint untuk mendapatkan detail buku berdasarkan ID
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book['id'] == id), None)
    if book:
        return jsonify(book)
    return jsonify({"message": "Buku tidak ditemukan"}), 404

# Endpoint untuk menambahkan buku baru
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = {"id": len(books) + 1, "title": data['title'], "author": data['author']}
    books.append(new_book)
    return jsonify(new_book), 201

# Endpoint untuk menghapus buku berdasarkan ID
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [book for book in books if book['id'] != id]
    return jsonify({"message": "Buku berhasil dihapus"}), 200

if __name__ == '__main__':
    app.run(debug=True)
