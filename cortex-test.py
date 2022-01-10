import socket
import sys
import struct
import time
import binascii

host = '10.163.155.106'
port = 3003

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

inputHex = binascii.unhexlify("499602d2000000280000000000000001000000010000000000000000b669fd2e")

try:
    #remote_ip = socket.gethostbyname(host)
    s.connect((host, port))

except socket.gaierror:

   print('Hostname could not be resolved Exiting')
   sys.exit()

   print('Socket connected to ' + host + ' on ip ')

try:
    s.send(inputHex)
    print('Message sent Successfully')
    time.sleep(1)

    print(inputHex)
    print('sending')


except socket.error:
    print('send fail')

    sys.exit()

print("ok")
a=input("")
