# Simple Python Port Scanner

This is a simple Python script for scanning a range of ports on a given IP address. It can be used to quickly identify open ports on a target machine.

## Features

- Scans a user-specified range of ports on a target IP address
- Reports which ports are open
- Simple and easy to use from the command line

## Usage

1. **Clone or Download this repository**

2. **Run the script**

```bash
python port_scanner.py <IP_ADDRESS> <START_PORT> <END_PORT>
```

**Example:**

```bash
python port_scanner.py 127.0.0.1 20 1024
```

This will scan ports from 20 to 1024 on `127.0.0.1` and print the open ports.

## Arguments

- `<IP_ADDRESS>`: The target IP address to scan.
- `<START_PORT>`: The first port in the range to scan.
- `<END_PORT>`: The last port in the range to scan.

## Requirements

- Python 3.x

No external dependencies are needed.

## Disclaimer

This tool is for educational purposes only. Please do not use it to scan networks or hosts without proper authorization.

