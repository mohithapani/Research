import socket;
import time;
s = socket.socket();
host = socket.gethostname();
port1 = 12399;
port2 = 12345;
s1 = socket.socket()
s.connect(('10.0.0.1',port1));
s1.connect(('10.0.0.2',port2));
#f = open('tosend.txt','rb');
print "Sending";

while(1):
	print "Sending...";
	time_sen = time.ctime(time.time())
	s.send(time_sen);
	s1.send(time_sen);
#f.close();
print "Done Sending";
s.shutdown(socket.SHUT_WR);
print s.recv(1024);
s.close();
