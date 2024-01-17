import socket

HOST_NAME = socket.gethostname()  # get  host name of your computer in local network
PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # INET is ipv4, SOCK_STREAM is TCP
s.connect((HOST_NAME, PORT))
msg = s.recv(100)  # buffer size
print(msg.decode("utf-8"))  # decode using utf-8 encoding

