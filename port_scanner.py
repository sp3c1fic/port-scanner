import time
import socket
from tqdm import tqdm


class Scanner:
    def __init__(self, ip_address, start_port, end_port):
        self.ip_address = ip_address
        self.start_port = start_port
        self.end_port = end_port

    def scan(self):

        open_ports = []
        for index, port in enumerate(tqdm(range(self.start_port, self.end_port + 1), desc="Scanning",
                                          unit="iteration",
                                          )):

            time.sleep(0.1)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            try:
                s.connect((self.ip_address, port))
                open_ports.append(port)
            except (ConnectionRefusedError, socket.timeout):
                pass
            except Exception as e:
                print(f'Something went wrong: {e}')
            finally:
                s.close()
        return open_ports
