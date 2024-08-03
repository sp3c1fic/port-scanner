# port-scanner
Main script for scanning open ports and extracting service banners. Conducts thorough port scans, identifies open ports, and retrieves detailed banners to gather information on network services.


PortHunter

PortHunter is a Python script designed to scan a range of ports on a specified IP address to detect open ports and retrieve associated banners. This tool is useful for network assessment and service identification.
Features:

    Scans for open ports within a user-defined range.
    Attempts to grab and display banners from open ports to identify services.

Usage:

    Clone the repository:

    bash

git clone [https://github.com/sp3c1fic/PortHunter.git](https://github.com/sp3c1fic/port-scanner)

Navigate to the project directory:

cd port-scanner

Run the script:


    python core.py -t [IP_ADDRESS] --start [START_PORT] --end [END_PORT]

        IP_ADDRESS: The target IP address.
        START_PORT: The beginning of the port range.
        END_PORT: The end of the port range.


Example usage screenshot:

![Screenshot at 2024-08-03 16-37-49](https://github.com/user-attachments/assets/9f918549-05c0-4323-8383-8cea7df6d445)


Example:

python core.py -t 192.168.1.1 --start 1 --end 1024


Requirements:

    Python 3.x
    socket library (standard library)
    argparse library (standard library)
    datetime (standard library)
    re (standard library)
    sys (standard library)


Example scan:

![Screenshot at 2024-08-03 16-25-41](https://github.com/user-attachments/assets/2fe4d14b-f05e-499a-8131-a371e2a882e4)


Note:

Ensure you have permission to scan the target IP address. Unauthorized scanning may be illegal or against network policies.
