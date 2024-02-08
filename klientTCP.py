import socket

def get_user_by_id(id):
    return f"/users/{id}"


def get_photos_id(id):
    return f"/photos/{id}"


def send_request(request):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8080))
    client.send(request.encode('utf-8'))
    response = client.recv(1024).decode('utf-8')
    print(f"Server response: {response}")
    client.close()


if __name__ == "__main__":
    id = 2
    request = get_user_by_id(id)
    send_request(request)