#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import socket
import rospy
from std_msgs.msg import String

HOST='192.168.1.105'

PORT=8008

BUFFER=4096

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind((HOST,PORT))

sock.listen(5)


rospy.init_node('tcptalker',anonymous=0)
pub=rospy.Publisher('tcptopic',String,queue_size=10)
con,addr=sock.accept()

print 'i am listening'

while not rospy.is_shutdown():
    try:
        #con.settimeout(5)
        buf=con.recv(BUFFER)
        print buf
        pub.publish(buf)  
        #time.sleep(1)
	#con.send('yes i recv')
    except socket.timeout:
        print 'time out'
    

con.close()
