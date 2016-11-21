import socket
import signal
def sigint_handle(sig,frame):
	try:
		pass
	except Exception:
		pass
	exit(0)

signal.signal(signal.SIGINT, sigint_handle);

s = socket.socket();
port = 12345;
s.bind(('10.0.0.5',port));
s.listen(5);
while True:
	client, addr = s.accept();
	print(" Got connection from" +  str(addr));
	print " Receiving ";
	l = client.recv(10)
	while(l):
		print l;
		print "Received";
	client.close();

s.shutdown(socket.shut_WR);
s.close();


