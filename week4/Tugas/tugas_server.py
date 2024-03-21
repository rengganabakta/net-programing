import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = 'localhost'
PORT = 12345

server_socket.bind((HOST, PORT))

server_socket.listen(1)
print("Waiting...")
client_socket, client_address = server_socket.accept()

data = client_socket.recv(1024)

angka = str(data.decode())
print("Request dari client :", angka, "IP client :", client_address)

message_length = len(data.decode())
response = f"Jumlah karakter pesan: {message_length}"
client_socket.sendall(response.encode())

client_socket.close()
server_socket.close()