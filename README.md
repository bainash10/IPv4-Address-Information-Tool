# IPv4 Network Details Calculator

This Python application built with Tkinter calculates and displays detailed information about IPv4 addresses, including network class, subnet mask, network ID, broadcast address, number of hosts per network, number of networks, network range, and hops.

## Features

- **IP Class Identification**: Determines if the entered IP address belongs to Class A, B, or C.
- **Subnet Mask Calculation**: Automatically generates the default subnet mask based on the IP class.
- **Network ID and Broadcast Address Calculation**: Calculates the network ID and broadcast address.
- **Hosts per Network Calculation**: Computes the number of usable hosts per network.
- **Number of Networks Calculation**: Calculates the total number of networks based on the subnet mask.
- **Network Range**: Displays the first and last usable IP addresses in the network range.
- **Hops Calculation**: Calculates the number of hops (usable hosts per network).

## Usage

1. **Input Format**: Enter an IPv4 address in the format X.X.X.X where X ranges from 0 to 255.
2. **Class A Range**: 1.0.0.0 to 126.255.255.255
3. **Class B Range**: 128.0.0.0 to 191.255.255.255
4. **Class C Range**: 192.0.0.0 to 223.255.255.255

## Requirements

- Python 3.x
- Tkinter library (usually comes pre-installed with Python)

## How to Run

1. Clone this repository.
2. Navigate to the directory containing `main.py`.
3. Run the script using Python:

Developed by [Nischal Baidar]
