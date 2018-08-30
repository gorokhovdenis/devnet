import sys
import telnetlib
import time
import socket
import re
import base64
#login with username and password
def login_user():
    num=0
    while num < len(user):
        print "function_username"
        try:
            time.sleep(2)
            tn.write(user[num]+'\r')
            time.sleep(2)
            tn.write(password[num]+'\r')
            time.sleep(2)
            passwd=tn.read_very_eager()
            result=re.search(r'#', passwd)
            if result:
                print 'start commands list'
                f2=open('/root/command.txt', 'r')
                string=f2.readlines()
                print '**********************'
                for line in string:
                    line=line[:-1]
                    print line
                    tn.write(line+'\r')
                    time.sleep(2)
                f2.close()
                print '**********************'
                print 'complete'
                break
            else:
                print "..."
            num +=1
        except IndexError:
            gotdata = 'null'
#login with  password and enable password
def login_password():
    j=0
    print "function_password"
    success=0
    try:
        tn.write(chmzpass+'\r')
        time.sleep(2)
        passwd=tn.read_eager()
        result=re.search(r'>', passwd)
        if result:
            tn.write('enable'+'\r\n')
            time.sleep(2)
            print 'try enable password'
            while success != 0 or j<len(en):
                passwd=tn.read_eager()
                result=re.search(r'Password:', passwd)
                if result:
                    print 'try #'+str(j)
                    tn.write(en[j]+'\r')
                    time.sleep(2)
                else:
                    print 'start commands list'
                    f2=open('/root/command.txt', 'r')
                    string=f2.readlines()
#                    print '**********************'
                    for line in string:
                        line=line[:-1]
#                        print line
                        tn.write(line+'\r')
                        time.sleep(2)
                    f2.close()
#                    print '**********************'
                    success=1
                    print 'complete'
                    break
                j +=1
    except IndexError:
        gotdata = 'null'
#enter
user = ['pi-telecom','cisco']
password = [base64.b64decode("aW5lcmZ0ZGhq"),base64.b64decode("Q2lzY282bzY2bzY=")]
chmzpass = base64.b64decode("Q0hNWmFkbWlu")
en = ['SW_mgr','Switch_mgr','RTR_mgr', 'Router_mhr', 'Router_mgr']
f1=open('/root/adr.txt', 'r')
s=f1.readlines()
for i in s:
	host=i[-17:-1]
	remote_host=host
	for remote_port in [23]:
	        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        	sock.settimeout(5)
	        try:
	                sock.connect((remote_host, remote_port))
	        except Exception,e:
	                print "port closed in ip "+host
			break
	        else: 
	                print "port open in ip "+host #% remote_port
			#login
			tn = telnetlib.Telnet(host)
			time.sleep(2)
   		        rawtext=tn.read_eager()
                        result=re.search(r'Userna', rawtext)
                        if result:
                            login_user()
                            print host
                            print "--------------------------------------"
                        else:
                            login_password()
                            print host
                            print "--------------------------------------"
		        time.sleep(2)
                        sock.close()
f1.close()
