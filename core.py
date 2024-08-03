import re
import sys
import socket
import argparse
import datetime
from grabber import Grabber
from port_scanner import Scanner

ARGUMENTS_LENGTH = 7


def is_ip_valid(ip_address):
    pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}'
                         r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$')
    return pattern.match(ip_address) is not None


def is_port_valid(port):
    return isinstance(port, int) and 1 <= port <= 65535


def print_banner():
    time_of_start = datetime.datetime.now().replace(second=0, microsecond=0)
    print(f'starting port scanner (https://github.com/sp3c1fic/port-scanner) at {time_of_start}')


def grab_banner(request, host, port):
    http_ports = [80, 8080, 8000]

    grabber = Grabber(host, port)
    try:
        if grabber.port in http_ports:
            grabber.s.send(request.encode())
        print(f'Printing banner for port {grabber.port}\n')
        print(grabber.read())
    except UnicodeDecodeError as e:
        print(f'Codec cannot be decoded. Banner cannot be grabbed: {e}')
    except socket.timeout as e:
        print(f'Error: {e}. Could not connect to port {grabber.port}\n')
    except socket.error as e:
        print(f'Connection Timed out: {e}')
    finally:
        grabber.close()


def process_arguments():
    parser = argparse.ArgumentParser(prog='Specter', description='An advanced, stealthy tool for discovering open '
                                                                 'ports on a network.')

    parser.add_argument('-t', '--target', help='Provide the IP address of a target that you want to scan.')
    parser.add_argument('--start', help='Provide the specified start port.')
    parser.add_argument('--end', help='Provide the specified end port.')
    args = parser.parse_args()
    return args, parser


def print_open_ports(sequence):
    [print(f'Port number: {port}') for port in sequence]


def main():
    args, parser = process_arguments()
    print_banner()

    if len(sys.argv) == ARGUMENTS_LENGTH:

        target = sys.argv[2]
        start_port = int(sys.argv[4])
        end_port = int(sys.argv[-1])

        if is_ip_valid(target) and is_port_valid(start_port) and is_port_valid(end_port):
            scanner = Scanner(target, start_port, end_port)
            open_ports = scanner.scan()

            print('\nFound open ports:\n')
            print_open_ports(open_ports)
            request = 'GET / HTTP/1.1\r\nHost: {}\r\nConnection: close\r\n\r\n'.format(target)
            for port in open_ports:
                grab_banner(request, target, port)
    else:

        if len(sys.argv) != ARGUMENTS_LENGTH:
            print(parser.print_help())
        else:
            if not is_ip_valid(sys.argv[2]) or not is_port_valid(sys.argv[4]) or not is_port_valid(sys.argv[-1]):
                print('[*] ERROR Invalid IP address or port format!')
                sys.exit(0)


if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        print('Terminating script... ')
        sys.exit(0)
