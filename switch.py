import sys
import telnetlib
import time
import socket

def zelax():
	#login
	#tn.read_until('login:')
	tn.write('tech\r')
	tn.read_until('Password:')
	tn.write('support\r')
	time.sleep(1)
	#SNTP client
	print 'Zelax  '+host
        tn.write('config\r')
	time.sleep(1)
        tn.write('sntp server 192.168.11.230\r')
	time.sleep(1)
        tn.write('sntp timezone Moscow add 4\r')
	time.sleep(1)
        tn.write('end\r')
	time.sleep(1)
        tn.write('copy running-config startup-config\r')
	time.sleep(8)

	
def des3028():
	#login
	time.sleep(3)
	tn.write('tech')
	tn.write('\n')
	tn.read_until('PassWord:')
	tn.write('support')
	tn.write('\n')
	print 'DES-3028 '+host
	tn.read_until('DES-3028')
	#SNTP client
	tn.write('enable sntp\r')
	time.sleep(1)
        tn.write('config sntp primary 192.168.11.230 secondary 0.0.0.0 poll-interval 100\r')
	time.sleep(1)
        tn.write('config time_zone operator + hour 4 min 0\r')
	time.sleep(1)
        tn.write('save\r')
	time.sleep(8)
	
def des3526():
	#login
	time.sleep(3)
	tn.write('tech')
	tn.write('\n')
	tn.read_until('password:')
	tn.write('support')
	tn.write('\n')	
	print 'DES-3526 '+host
	time.sleep(1)
	#tn.read_until('DES-3526:admin#')
	tn.write('enable sntp\r')
	time.sleep(1)
        tn.write('config sntp primary 192.168.11.230 secondary 0.0.0.0 poll-interval 100\r')
	time.sleep(1)
        tn.write('config time_zone operator + hour 4 min 0\r')
	time.sleep(1)
        tn.write('save\r')
	time.sleep(8)
	
def firmware_zelax():
	#login
	tn.read_until('login:')
	tn.write('tech\r')
	tn.read_until('Password:')
	tn.write('support\r')
	time.sleep(1)
	#tn.write('enable\r')
        #Download nos.img
        tn.write('copy tftp://192.168.1.151/1/nos.img nos.img')
        tn.write('\r')
        tn.read_until('Confirm copy file')
        tn.write('y\r')
        print ('download is running. Please wait a minute.')
        tn.read_until('close tftp client')
        time.sleep(2)
        #download boot.rom
        tn.write('copy tftp://192.168.1.151/1/boot.rom boot.rom')
        tn.write('\r')
        tn.read_until('Confirm copy file')
        tn.write('y\r')
        tn.read_until('close tftp client')
        print ('boot.rom download success')
        time.sleep(1)
        #download vendor.cfg
        tn.write('copy tftp://192.168.1.151/1/vendor.cfg vendor.cfg')
        tn.write('\r')
        tn.read_until('Confirm copy file')
        tn.write('y\r')
        tn.read_until('close tftp client.')
        print ('vendor.cfg download success')
        time.sleep(1)
        #config.rom
        tn.write('copy tftp://192.168.1.151/1/config.rom config.rom')
        tn.write('\r')
        tn.read_until('Confirm copy file')
        tn.write('y\r')
        tn.read_until('close tftp client.')
        print ('Download success. Device is reboot now')
        time.sleep(1)
        #
        tn.write('reload\r')
        time.sleep(2)
        tn.write('y\r')
        print host

def whois():
	B=['DES-3028','DES-3526','Verification','login']
        j=0
        global tn
	tn = telnetlib.Telnet(host)
        while j<4:
                tmp=''
                time.sleep(1)
                tmp=tn.read_until(B[j],3)
                if tmp.find(B[j]) != -1:
                        return B[j]
                        tn.close()
                        break
                else:
                        j=j+1
                        tn.close()
                        tn = telnetlib.Telnet(host)
	

	
#enter
user = 'user'
password = 'password'
f1=open('/home/goroshik/tmp/adr.txt', 'r')
s=f1.readlines()
a=0
for i in s:
	host=i[-17:-1]
	remote_host=host
	for remote_port in [23]:
	        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        	sock.settimeout(3)
	        try:
	                sock.connect((remote_host, remote_port))
	        except Exception,e:
	                print "port closed in ip "+host
			break

	        else: 
	                # print "port open in ip "+host #% remote_port
			model=whois()
			if model == 'DES-3028':
				des3028()
			elif model == 'DES-3526':
				des3526()
			elif model == 'Verification':
				edgecore()	
			elif model == 'login':
				zelax()	
	        sock.close()

#                       tmp=tn.read_some()
#                       if tmp.find('>') != -1:
#                               fmw()


