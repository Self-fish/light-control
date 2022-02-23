import socket


class SocketServer:

    def __init__(self, port):
        self.__service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__service.bind(("", port))
        self.__service.listen(1)

    def listen_messages(self, handle_message):
        while True:
            client, address = self.__service.accept()
            try:
                while True:
                    message = client.recv(1024)
                    if message:
                        handle_message(message)
                    else:
                        break
            finally:
                client.close()
