import socket

def Main():
    UDP_IP_ADDRESS = "0.0.0.0"
    UDP_PORT_NO = 8890


    serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

    while True:
        data, addr = serverSock.recvfrom(1024)
        print "Message: ", data

if __name__ == '__main__':
    Main()
