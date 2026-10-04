import socket
from datetime import datetime


def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    try:
        result = sock.connect_ex((host, port))

        if result == 0:
            return True

    except socket.error:
        pass

    finally:
        sock.close()

    return False


def main():
    target = input("Enter an authorized host (e.g. localhost): ").strip()

    if not target:
        print("No host was entered.")
        return

    try:
        ip_address = socket.gethostbyname(target)
    except socket.gaierror:
        print("Could not resolve the host.")
        return

    print("\n------------------------------")
    print("Local Port Scanner")
    print("------------------------------")
    print("Target:", target)
    print("IP Address:", ip_address)
    print("Started:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("------------------------------")

    open_ports = []

    for port in range(1, 101):
        if scan_port(ip_address, port):
            open_ports.append(port)
            print(f"Port {port}: OPEN")

    print("------------------------------")

    if open_ports:
        print("Open ports found:", len(open_ports))
    else:
        print("No open ports found in the selected range.")

    print("Scan completed.")


if __name__ == "__main__":
    main()
