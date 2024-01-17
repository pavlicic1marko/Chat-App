import socket

HOST_NAME = socket.gethostname()  # get  host name of your computer in local network
PORT = 12344

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # INET is ipv4, SOCK_STREAM is TCP
s.connect((HOST_NAME, PORT))
msg1 = s.recv(10)  # buffer size, argument is the number of bytes
print(msg1.decode("utf-8"))  # decode using utf-8 encoding
msg2 = s.recv(10)
print(msg2.decode("utf-8"))
