import socket
import ssl

def start_client():
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_verify_locations("server.crt")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 12345))
    client_socket = context.wrap_socket(client_socket, server_hostname="reng")

    print("Connected to server.")

    while True:
        message = input("You: ")
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(f"Server: {data}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
