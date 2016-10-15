#anthrax_listener 1.0
port = 22
version = 'anthrax_listener_1.0'
#-------------------------------------------------------
print version + ' starting...'
#-------------------------------------------------------
#imported from firebug v4.1
import sys, shutil, os, time
#client functions:
def status(location='C:/python27/log.txt'):
    status = 'None'
    if os.path.exists(location):
        try:
            os.rename(location,location.replace('/log.txt', '/logg.txt'))
            os.rename(location.replace('/log.txt', '/logg.txt'), location)
        except OSError:
            print 'Status: Active'
            status = 'Status: Active'
        else:
            print 'Status: Inactive'
            status = 'Status: Inactive'
        
        print 'Log found in: ' + location
        status = status + '\n Log found in:' + location
        f = open(location, 'r')
        data = f.readlines()
        print 'Log size: ' + str(len(data)) + ' Characters'
        status = status + '\n Log size: ' + str(len(data)) + ' Characters'
    else:
        print 'No log found in: ' + location
        status = status + '\n No log found in: ' + location
    return status
        

#-------------------------------------------------------
#!/usr/bin/python           # This is client.py file
exceptions = 0
import socket               # Import socket module
def sock():
    global s, host
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    connected=False
    while connected==False:
        try:
            s.connect((host, port))
            s.send(version + '@' + str(host))
            connected=True
            #print 'Connected'
        except:
            print 'Connecting failed...'
sock()
while True:
    global s, host
    try:
        recv = s.recv(2048)
        print recv
        if (recv=='get_log'):
            s.send('Log hier')
        elif (recv=='status'):
            s.send(status())
        else:
            s.send('Server error')
        exceptions=0
    except Exception as e:
        print 'connection error: '
        print e
        exceptions+=1
        if exceptions>=10:
            print 'reconnecting...'
            sock()
            
        
s.close                     # Close the socket when done
#--------------------------------------------------------


print 'Listener End..'
