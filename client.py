import socket;
import time;
s = socket.socket();
host = socket.gethostname();
port = 12345;

s.connect(('10.0.0.5',port));
#f = open('tosend.txt','rb');
print "Sending";

while(1):
	print "Sending...";
	time_sen = time.ctime(time.time())
	s.send(time_sen);
#f.close();
print "Done Sending";
s.shutdown(socket.SHUT_WR);
print s.recv(1024);
s.close();
