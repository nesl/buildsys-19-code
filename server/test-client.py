"""
    This file is for testing purpose only. We do not use this file
    for the real usage.
"""

import socket
import sys

HOST, PORT = '172.17.52.6', 9999
data = ' '.join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall((data + '\n').encode('utf-8'))

    # Receive data from the server and shut down
    received = sock.recv(1024)
finally:
    sock.close()

print('Sent:     {}'.format(data))
print('Received: {}'.format(received.decode('utf-8')))
