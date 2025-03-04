import socket as s

# CLIENT, IF YOU CONNECTED

MAX_BUFFER_SIZE = 10240
# Step 1 - Setup
my_socket = s.socket(type=s.SOCK_STREAM) # USE TCP (This is the default)

# Step 2 - start Conversation
destination = ("130.111.118.165", 2025) # Must be a tuple

my_socket.connect(destination)

# Step 3 - send and Receive
data = my_socket.recv(MAX_BUFFER_SIZE)
msg = ""
while msg.decode() != "quit":
    msg = bytes(input("new msg: "))
    my_socket.sendall(msg)

    

my_socket.close()
# Decoding the data

"""
master_socket = s.socket(type=s.SOCK_STREAM) # TCP socket

my_addr = ("", 2025)

master_socket.bind(my_addr) # Needs a tuple. like connect() does

master_socket.listen(5)

# Step 2 - Start the Conversation

(client_socket, client_addr) = master_socket.accept()

(client_ip, client_port) = client_addr
print("Connection from", client_ip, "port", client_port)

# Step 3 - send and receive
my_str = "Hello From a python TCP server\r\n"

my_bytes = my_str.encode()

print("sending my message")
client_socket.sendall(my_bytes)

# Step 4 - end the convo
client_socket.close()

master_socket.close()
"""