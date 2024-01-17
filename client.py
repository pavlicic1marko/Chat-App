import socket

HOST_NAME = socket.gethostname()  # get  host name of your computer in local network
PORT = 12344

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # INET is ipv4, SOCK_STREAM is TCP
s.connect((HOST_NAME, PORT))

while True:
    message = ''
    while True:
        msg = s.recv(10)
        if len(msg) <= 0:
            break
        message += msg.decode("utf-8")
    if len(message) > 0:
        print(message)
