import socket

# Inisialisasi objek socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tentukan alamat server yang akan dihubungi
server_address = ('localhost', 8888)  # Misalnya, server di localhost dengan port 8888

# Terhubung ke server
client_socket.connect(server_address)

try:
    # Kirim pesan ke server
    message = "Halo, ini pesan dari client!"
    client_socket.sendall(message.encode())

    # Terima balasan dari server
    received_data = client_socket.recv(1024)
    print("Diterima dari server:", received_data.decode())

finally:
    # Tutup koneksi dengan server
    client_socket.close()
