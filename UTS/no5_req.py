import requests

# URL of the Flask REST API endpoint
url = 'http://localhost:5000/books'

# Data for the new book (get input from user)
book_title = input("Masukkan judul buku: ")
book_author = input("Masukkan nama penulis: ")

data = {
    "title": book_title,
    "author": book_author
}

# Send POST request to add a new book
response = requests.post(url, json=data)

# Check if the request was successful
if response.status_code == 201:
    print("Buku berhasil ditambahkan:")
    print(response.json())  # Print the details of the newly added book
else:
    print("Gagal menambahkan buku. Kode status respons:", response.status_code)
