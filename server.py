import socket
import config_parser


HOST_NAME = socket.gethostname()  # get  host name of your computer in local network
print(HOST_NAME)
PORT = config_parser.get_port()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # INET is ipv4, SOCK_STREAM is TCP
s.bind((HOST_NAME, PORT))
s.listen(4)  # backlog , number of unaccepted connections
client, address = s.accept()

while True:
    message = input('Server:')
    client.send(bytes(message, "utf-8"))  # encode into bytes using utf-8 encoding

    message_from_client = client.recv(100)
    print("client: " + message_from_client.decode('utf-8'))

