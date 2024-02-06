# Import the 'socket' module to work with network-related functions.
import socket

# The following code retrieves the local IP address of the current machine:
# 1. Use 'socket.gethostname()' to get the local hostname.
# 2. Use 'socket.gethostbyname_ex()' to get a list of IP addresses associated with the hostname.
# 3. Filter the list to exclude any IP addresses starting with "127." (loopback addresses).
# 4. Extract the first IP address (if available) from the filtered list.
# 5. Print the obtained IP address to the console.

# Step 1: Get the local hostname.
local_hostname = socket.gethostname()

# Step 2: Get a list of IP addresses associated with the hostname.
ip_addresses = socket.gethostbyname_ex(local_hostname)[2]

# Step 3: Filter out loopback addresses (IPs starting with "127.").
filtered_ips = [ip for ip in ip_addresses if not ip.startswith("127.")]

# Step 4: Extract the first IP address (if available) from the filtered list.
first_ip = filtered_ips[:1]

# Step 5: Print the obtained IP address to the console.
print(first_ip[0])