import socket


class Grabber:

    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.settimeout(5)

        try:
            self.s.connect((self.ip_address, self.port))
        except Exception as e:
            print(f"Failed to connect to {self.ip_address}:{self.port} - {e}")

    def read(self):
        return self.s.recv(1024).decode('utf-8')

    def close(self):
        self.s.close()


