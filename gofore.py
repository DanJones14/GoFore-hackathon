import socket
import time

def Main():
    while True:
        UDP_IP_ADDRESS = "192.168.10.1"
        UDP_PORT_NO = 8889



        clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


        inputCommand = raw_input("Enter Command: ")

        if inputCommand == "command":
            Message = "command"
            clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))

        #Message = "command"
        #clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))

        if inputCommand == "takeoff":
            Message = "takeoff"
            clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))

        if inputCommand == "land":
            Message = "land"
            clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))

    #clientSock.listen(1)


if __name__ == '__main__':
    Main()
