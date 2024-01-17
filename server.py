import socket

HOST_NAME = socket.gethostname()  # get  host name of your computer in local network
print(HOST_NAME)
PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # INET is ipv4, SOCK_STREAM is TCP
s.bind((HOST_NAME, PORT))
s.listen(4)  # backlog , number of unaccepted connections

while True:
    client, address = s.accept()
    print('Client is connected and hase the address: ' + str(address))

