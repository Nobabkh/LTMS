import socket
import sys
def req(latitude1, longitude1, latitude2, longitude2):
    soc = socket.socket(socket.AF_INET) #initializing the socket
    HOST = '127.0.0.1'
    PORT = 8888
    # latitude1 = float(sys.argv[1])
    # longitude1 = float(sys.argv[2])
    # latitude2 = float(sys.argv[3])
    # longitude2 = float(sys.argv[4])
    soc.connect((HOST,PORT))
    final = str(latitude1)+' '+str(longitude1)+' '+str(latitude2)+' '+str(longitude2)
    soc.send(final.encode())
    return soc.recv(1024).decode()