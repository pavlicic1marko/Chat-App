import socket
import config_parser

HOST_NAME = socket.gethostname()  # get  host name of your computer in local network
PORT = config_parser.get_port()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # INET is ipv4, SOCK_STREAM is TCP
s.connect((HOST_NAME, PORT))

while True:
    message = s.recv(100)
    print("server:" + message.decode('utf-8'))

    message_to_send = input('Client:')
    s.send(bytes(message_to_send, "utf-8"))
