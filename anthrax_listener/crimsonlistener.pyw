print 'Listener running...'
#f = open('C://Python27/listener.txt','w')
#f.write('hoi')
#f.close()
#-------------------------------------------------------
#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 22222                # Reserve a port for your service.

s.connect((host, port))
s.send('Connected')
while True:
    recv = s.recv(1024)
    print recv
    if (recv=='get_log'):
        s.send('Log hier')
    if (recv=='close'):
        s.close()
#s.close                     # Close the socket when done
#--------------------------------------------------------


print 'Listener End..'
