import socket
import config_parser


HOST_NAME = socket.gethostname()  # get  host name of your computer in local network
print(HOST_NAME)
PORT = config_parser.get_port()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # INET is ipv4, SOCK_STREAM is TCP
s.bind((HOST_NAME, PORT))
s.listen(4)  # backlog , number of unaccepted connections

while True:
    client, address = s.accept()
    client.send(bytes("Hallo World, test","utf-8"))  # encode into bytes using utf-8 encoding
    print('Client is connected and hase the address: ' + str(address))
    client.close()  # close connection

