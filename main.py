

import socket
import argparse

class OpenNet:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        print("connected to:", host, port)

    def close(self):
        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()

    def mftpSend(self, data, info):
        print(info, data)
        self.sock.send(data.encode("utf-8"))
        print("done")

    def mftpRecv(self, info):
        recv = self.sock.recv(1024)
        print(info, recv.decode("utf-8"))
        print("done")


class Package:
    def mftp(self, V, I, A, C, R, SEPT):
        self.V    = V      #version naber
        self.I    = I      # id
        self.A    = A      # auth type
        self.C    = C      # chipher type
        self.R    = R      # network addr
        self.SEPT = SEPT   #random 8 byte in hex

    def INF7(self):
        self.INF7 = "INF V=%s I=%s A=%s C=%s R=%s 7=%s" % (self.V, self.I, self.A, self.C, self.R, self.SEPT)
        return self.INF7

    def PUT(self, data):
        return "PUT %s" % data

#def fuckingNet(inf, put

def fuckingFuzz(portList, INF7, PUT):
    for p in portList:
        on = OpenNet('192.168.10.1', p)
        on.mftpSend(INF7, "Sended INF7 package:")
        on.mftpRecv("Recived INF8 package:")
        on.mftpSend(PUT, "Sended PUT package:")
        on.mftpRecv("Recived PUT package:")
        payload = 'A' * 1000
        iter = 0
        for ii in range(0, len(payload), 1000):
            iter +=1
            on.mftpSend(payload[ii:ii+1000], " Sended payload data:" )

        on.close()    


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
## V=%s I=%s A=%s C=%s R=%s 7=%s
    parser.add_argument("-v", "--version", type=str, help="Version mftp protocol")
    parser.add_argument('-i', "--id", type=str, help="User id")
    parser.add_argument('-a', "--auth_type", type=str, help="Type of authentification")
    parser.add_argument('-c', "--chipher", type=str, help="Chipher mode")
    parser.add_argument('-r', "--network", type=str, help="Network user address (id)")
    parser.add_argument('-s', "--random", type=str, help="Random")

    args = parser.parse_args()

    p = Package()
    p.mftp(args.version, args.id, args.auth_type, args.chipher, args.network, args.random)

    INF7 = p.INF7()
    PUT = p.PUT("F=fil.txt L=255 P=255 F=fil.txt L=255 P=255 F=fil.txt L=255 "
                "P=255 F=fil.txt L=255 P=255 F=fil.txt L=255 P=255 F=fil.txt "
                "L=255 P=255 F=fil.txt L=255 P=255 F=fil.txt L=255 P=255 F=fil.txt"
                " L=255 P=255 F=fil.txt L=255 P=255 F=fil.txt L=255 P=255 F=fil.txt"
                " L=255 P=255 F=fil.txt L=255 P=255 F=fil.txt L=255 P=255 F=fil.txt"
                " L=255 P=255 F=fil.txt L=255 P=255 F=fil.txt L=255 P=255 F=fil.txt"
                " L=255 P=255 F=fil.txt L=255 P=255 F=fil.txt L=255 P=255 F=fil.txt"
                " L=255 P=255 F=fil.txt L=255 P=255 F=fil.txt L=255 P=255 F=fil.txt "
                "L=255 P=25")

fuckingFuzz([5000, 5001, 5002, 5100], INF7, PUT)

'''
    on = OpenNet('192.168.10.1', 5001)
    on.mftpSend(INF7, "Sended INF7 package:")
    on.mftpRecv("Recived INF8 package:")
    on.mftpSend(PUT, "Sended PUT package:")
    on.mftpRecv("Recived PUT package:")
    payload = 'A' * 1000
    iter = 0
    for ii in range(0, len(payload), 1000):
        iter +=1
        on.mftpSend(payload[ii:ii+1000], " Sended payload data:" )

    on.close()
'''