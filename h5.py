import socket
import signal
import threading
def sigint_handle(sig,frame):
	try:
		pass
	except Exception:
		pass
	exit(0)

signal.signal(signal.SIGINT, sigint_handle);
def Thread1():
	print("Starting Thread1")
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
			#print l;
			print "Received";
		client.close();

	s.shutdown(socket.shut_WR);
	s.close();

def Thread2():
	print("Starting Thread2")
	s2 = socket.socket();
	port = 12346;
	s2.bind(('10.0.0.5',port));
	s2.listen(5);
	while True:
		client, addr = s2.accept();
		print(" Got connection from" +  str(addr));
		print " Receiving ";
		l = client.recv(10)
		while(l):
			#print l;
			print "Received";
		client.close();

	s.shutdown(socket.shut_WR);
	s.close();

try:
	a = threading.Thread(target=Thread1,);
	a.start();
	b = threading.Thread(target = Thread2,);
	b.start();
except:
	print "Error in starting threads";
