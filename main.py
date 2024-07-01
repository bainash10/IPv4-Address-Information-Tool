import tkinter as tk
from tkinter import messagebox

def validate_ip(ip):
    # Check if IP is valid IPv4 format
    octets = ip.split('.')
    if len(octets) != 4:
        return False
    for octet in octets:
        if not octet.isdigit():
            return False
        if not (0 <= int(octet) <= 255):
            return False
    # Handle special cases for 0.0.0.0 and 255.255.255.255
    if ip == '0.0.0.0' or ip == '255.255.255.255':
        return False
    return True

def determine_ip_class(ip):
    first_octet = int(ip.split('.')[0])
    if 1 <= first_octet <= 126:
        return 'A', '255.0.0.0'
    elif 128 <= first_octet <= 191:
        return 'B', '255.255.0.0'
    elif 192 <= first_octet <= 223:
        return 'C', '255.255.255.0'
    else:
        return 'Unknown', 'N/A'

def calculate_network_address(ip, subnet_mask):
    # Calculate network address
    ip_octets = ip.split('.')
    mask_octets = subnet_mask.split('.')
    network_octets = []
    for i in range(4):
        network_octets.append(str(int(ip_octets[i]) & int(mask_octets[i])))
    network_address = '.'.join(network_octets)
    return network_address

def calculate_broadcast_address(ip, subnet_mask):
    # Calculate broadcast address
    ip_octets = ip.split('.')
    mask_octets = subnet_mask.split('.')
    inverted_mask_octets = [str(255 - int(mask_octet)) for mask_octet in mask_octets]
    broadcast_octets = []
    for i in range(4):
        broadcast_octets.append(str(int(ip_octets[i]) | int(inverted_mask_octets[i])))
    broadcast_address = '.'.join(broadcast_octets)
    return broadcast_address

def calculate_hosts_per_network(subnet_mask):
    # Calculate number of hosts per network
    mask_octets = subnet_mask.split('.')
    host_bits = sum(bin(int(octet)).count('1') for octet in mask_octets)
    return 2**(32 - host_bits) - 2  # subtract 2 for network and broadcast addresses

def calculate_number_of_networks(subnet_mask):
    # Calculate number of networks
    mask_octets = subnet_mask.split('.')
    host_bits = sum(bin(int(octet)).count('1') for octet in mask_octets)
    return 2**(32 - host_bits)

def calculate_network_range(network_address, subnet_mask):
    # Calculate network range (first and last usable addresses)
    ip_octets = network_address.split('.')
    mask_octets = subnet_mask.split('.')
    inverted_mask_octets = [str(255 - int(mask_octet)) for mask_octet in mask_octets]
    start_octets = []
    end_octets = []
    for i in range(4):
        start_octets.append(ip_octets[i])
        end_octets.append(str(int(ip_octets[i]) | int(inverted_mask_octets[i])))
    
    start_address = '.'.join(start_octets)
    end_address = '.'.join(end_octets)
    
    return start_address, end_address

def calculate_hops(subnet_mask):
    # Calculate hops (number of hosts per network)
    mask_octets = subnet_mask.split('.')
    host_bits = sum(bin(int(octet)).count('1') for octet in mask_octets)
    return 2**(32 - host_bits)

def on_submit():
    ip = entry_ip.get()
    if validate_ip(ip):
        ip_class, subnet_mask = determine_ip_class(ip)
        network_address = calculate_network_address(ip, subnet_mask)
        broadcast_address = calculate_broadcast_address(ip, subnet_mask)
        hosts_per_network = calculate_hosts_per_network(subnet_mask)
        number_of_networks = calculate_number_of_networks(subnet_mask)
        start_address, end_address = calculate_network_range(network_address, subnet_mask)
        hops = calculate_hops(subnet_mask)
        
        result = (
            f"IP Class: {ip_class}\n"
            f"Default Subnet Mask: {subnet_mask}\n"
            f"Network ID: {network_address}\n"
            f"Broadcast Address: {broadcast_address}\n"
            f"Hosts per Network: {hosts_per_network}\n"
            f"Number of Networks: {number_of_networks}\n"
            f"Network Range: {start_address} - {end_address}\n"
            f"Hops (Usable Hosts per Network): {hops}"
        )
        messagebox.showinfo("IP Details", result)
    else:
        messagebox.showerror("Error", "Invalid IP address format. Please enter a valid IPv4 address.")

# Create a Tkinter window
root = tk.Tk()
root.title("IP Details Calculator")

# Styling and Layout
root.geometry("500x400")
root.resizable(False, False)

# Create and place widgets
label_rules = tk.Label(root, text="Rules:\n"
                                 "1. Enter an IPv4 address in the format X.X.X.X where X ranges from 0 to 255.\n"
                                 "2. Class A ranges from 1.0.0.0 to 126.255.255.255.\n"
                                 "   - Network ID format: N.H.H.H\n"
                                 "   - Default Subnet Mask: 255.0.0.0\n"
                                 "   - Uses: Typically used by very large organizations and ISPs.\n\n"
                                 "3. Class B ranges from 128.0.0.0 to 191.255.255.255.\n"
                                 "   - Network ID format: N.N.H.H\n"
                                 "   - Default Subnet Mask: 255.255.0.0\n"
                                 "   - Uses: Commonly used by medium to large-sized networks like universities and businesses.\n\n"
                                 "4. Class C ranges from 192.0.0.0 to 223.255.255.255.\n"
                                 "   - Network ID format: N.N.N.H\n"
                                 "   - Default Subnet Mask: 255.255.255.0\n"
                                 "   - Uses: Suitable for smaller networks such as small businesses and home networks.")
label_rules.pack(pady=10)

label_example = tk.Label(root, text="Example: 192.168.1.1")
label_example.pack()

label_ip = tk.Label(root, text="Enter IPv4 address:")
label_ip.pack(pady=5)

entry_ip = tk.Entry(root, width=30)
entry_ip.pack()

button_submit = tk.Button(root, text="Submit", command=on_submit)
button_submit.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
