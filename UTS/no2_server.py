import socket

# Inisialisasi objek socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding ke alamat dan port tertentu
server_address = ('localhost', 8888)  # Misalnya, localhost dengan port 8888
server_socket.bind(server_address)

# Mendengarkan koneksi yang masuk
server_socket.listen(5)  # Maksimal 5 koneksi dalam antrian

print("Menunggu koneksi...")

while True:
    # Menerima koneksi dari client
    client_socket, client_address = server_socket.accept()

    print(f"Terhubung dengan {client_address}")

    # Menerima data dari client
    data = client_socket.recv(1024)
    if data:
        print("Diterima:", data.decode())

        # Mengirim balasan kembali ke client
        client_socket.sendall(b"Terima kasih atas pesan Anda!")

    # Tutup koneksi dengan client
    client_socket.close()
