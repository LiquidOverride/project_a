#anthrax_commander_lib
lib_version = '2'
#--------------------------------------------
def init(arg):
    global c
    c = arg
def lib_version():
    print 'anthrax_commander_lib version: ' + lib_version
#--------------------------------------------
def get_log():
    c.send('get_log')
    recv = c.recv(2048)
    print recv
def status():
    c.send('status')
    recv = c.recv(2048)
    print recv    
