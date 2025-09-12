import socket

def scan_ports(ip, start_port, end_port, timeout=0.5):
    open_ports = []
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
            result = s.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
        except Exception as e:
            pass
        finally:
            s.close()
    return open_ports

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Simple port scanner")
    parser.add_argument("ip", help="Target IP address to scan")
    parser.add_argument("start_port", type=int, help="Starting port number")
    parser.add_argument("end_port", type=int, help="Ending port number")
    args = parser.parse_args()

    print(f"Scanning {args.ip} from port {args.start_port} to {args.end_port}...")
    open_ports = scan_ports(args.ip, args.start_port, args.end_port)

    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("No open ports found in the specified range.")
