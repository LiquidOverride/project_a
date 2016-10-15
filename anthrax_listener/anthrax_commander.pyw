#anthrax_commander 1.1
port = 22
#----------------------------------------------------
#!/usr/bin/python           # This is server.py file
import socket               # Import socket module
import urllib2, urllib, shutil
#from anthrax_commander_lib import *
#----------------------------------------------------
def import_lib():
    url_lib = "https://dl.dropboxusercontent.com/u/42966918/anthrax/anthrax_listener/anthrax_commander_lib.py?dl=1"
    print 'Downloading lib...',
    lib = urllib.URLopener()
    lib.retrieve(url_lib, "anthrax_commander_lib.py")
    print 'Done'
    print 'Installing lib...',
    global anthrax_commander_lib, lib
    import anthrax_commander_lib as lib
    print 'Done'
def conn():
    global c, addr
    c, addr = s.accept()
    recv = c.recv(2048)
    print 'Got connection from', addr, recv
    #init(c)
def commander():
    global addr
    try:
        i = input(str(addr)+'#>')
    except Exception as e:
        print 'invalid command'
        print e
        commander()
def send(command):
    response = False
    c.send(command)
    recv = c.recv(2048)
    print recv
def close():
    c.close()
    addr = '127.0.0.1'
#----------------------------------------------------
print 'anthrax_commander_1.0'
def sock():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = socket.gethostname()
    s.bind((host, port))
    print 'Waiting for connection...'
    s.listen(100)
    conn()
addr = '127.0.0.1'
#sock()
while True:
    commander()
   
