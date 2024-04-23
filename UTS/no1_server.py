import socket
import ssl

def start_server():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 12345))
    server_socket.listen(1)

    print("Server is listening...")

    while True:
        conn, addr = server_socket.accept()
        conn = context.wrap_socket(conn, server_side=True)
        print(f"Connected to {addr}")

        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"Client: {data}")
            response = input("You: ")
            conn.send(response.encode())

        conn.close()

if __name__ == "__main__":
    start_server()
