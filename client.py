import socket;
import time;
import json;
from sine import generate_wave;
from test import *
s = socket.socket();
host = socket.gethostname();
port1 = 12399;
port2 = 12345;
s1 = socket.socket()
s.connect(('10.0.0.1',port1));
s1.connect(('10.0.0.2',port2));
#f = open('tosend.txt','rb');
print "Sending";
wave = {}
k = 1
while(k):
	print "Sending...";
	#time_sen = time.ctime(time.time())
	signal = generate_wave()

	for a in range(0,len(signal)):
		s.send("{:.5f}\n".format(signal[a]));
		s1.send(signal[a]);
	k = 0;
#f.close();
print "Done Sending";
s.shutdown(socket.SHUT_WR);
print s.recv(1024);
s.close();
