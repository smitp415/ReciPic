import socket
import os
import io
from PIL import Image
from array import array


def readimage(path):
    count = os.stat(path).st_size / 2
    with open(path, "rb") as f:
        return bytearray(f.read())

def Main():
   host = '192.168.70.246' #HOST
   port = 5001            #PORT

   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.bind((host,port))
   print("listening")
   s.listen(1)
   c, addr = s.accept()
   print("Connection from: " + str(addr))
   buf = ''
   while len(buf)<4:
     buf += c.recv(4-len(buf))
   size = struct.unpack('!i', buf)
   print("receiving %s bytes") % (size)

   i = 0
   with open('img/test.jpg', 'wb') as img:
     while True:
        data = c.recv(1024)
        if not data:
            break
        img.write(data)
     c.close()



if __name__ == '__main__':
   Main()