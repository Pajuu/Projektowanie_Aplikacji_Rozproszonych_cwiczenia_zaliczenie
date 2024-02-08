import socket
import threading
import json
from urllib.parse import urlparse

users = {
    "1": {"Imie": "Adam", "Nazwisko": "Nowak", "Nick": "randomNick123"},
    "2": {"Imie": "Jan", "Nazwisko": "Kowalski", "Nick": "warhammer41"}
}


photos = {
    "1": "https://images.pexels.com/photos/572861/pexels-photo-572861.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "2": "https://images.pexels.com/photos/10727524/pexels-photo-10727524.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
}


def get_users_id(id):
    return users.get(id, "Nie znaleziono uzytkownika o takim ID")

def get_photos_id(id):
    return photos.get(id, "Nie znaleziono uzytkownika o takim ID")


def handle_client(client_socket):
    request = client_socket.recv(1024).decode('utf-8')

    try:
        parsed_path = urlparse(request)
        path = parsed_path.path
        if path.startswith("/users/"):
            id = path.split("/")[-1]
            response = json.dumps(get_users_id(id))
        elif path.startswith("/photos/"):
            id = path.split("/")[-1]
            response = json.dumps(get_photos_id(id))
        else:
            response = "Niepoprawne zapytanie"
    except Exception as e:
        response = f"Error: {str(e)}"

    client_socket.send(response.encode('utf-8'))
    client_socket.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8080))
    server.listen(5)
    print("Port: 0.0.0.0:8080")

    while True:
        client, addr = server.accept()
        print(f"Zaakceptowano polaczenie od {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


if __name__ == "__main__":
    start_server()