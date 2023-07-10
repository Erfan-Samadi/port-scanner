import socket


def scan(target_ip, ports):
    for port in range(1, ports):
        scan_port(target_ip, port)


def scan_port(ip_address, port):
    # initializing the socket to communicate with port
    try:
        sock = socket.socket()
        sock.connet((ip_address, port + 1))
        print(f"[+] port is open {str(port)}")
        sock.close()

    except:
        pass
    # if it manage to connect to port it means port is open otherwise it means port is close


targets = input("IP address of the targets (split them by `,`): ")
ports_number = int(input("How many ports should I scan: "))

if "," in targets:
    print("[*] scanning multiple targets...")
    for ip in targets.split(","):
        scan(ip.strip(" "), ports_number)
else:
    print("[*] scanning single target...")
    scan(targets.strip(" "), ports_number)


