# Scott Rousseau
# Basic FTP File Fuzzer
# For Educational Purposes

import sys, socket
from time import sleep

target = sys.argv[1]
buffer=["A"]
counter=2

while True:
    try:
        print "Buffer is now" + str(buffer)
        commands=["MKD", "GET", "STOR"]
        for command in commands:
            for string in buffer:
                print "Sending buffer with length: "+str(len(buffer))
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.settimeout(5)
                # IP to run against
                connect=s.connect((target,21))
                s.recv(1024)
                s.send('USER ftp\r\n')
                s.recv(1024)
                s.send('PASS ftp\r\n')
                s.recv(1024)
                s.send(command+' '+string+'\r\n')
                s.recv(1024)
                s.send('QUIT ftp \r\n')
                s.close()
                sleep(1)
        buffer.append("A"*50)
    except:
        print "Something happened when buffer length: " + str(len(buffer)-50)
        sys.exit()
