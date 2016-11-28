import socket
import signal
import threading
import time
def sigint_handle(sig,frame):
	try:
		pass
	except Exception:
		pass
	exit(0)


def Thread1():


	print("Starting Thread1")
	s = socket.socket();
	port = 12345;
	s.bind(('10.0.0.5',port));
	s.listen(5);
	while True:
		client, addr = s.accept();
		print(" Got connection from" +  str(addr));
		#print " Receiving ";
		l = client.recv(10)
		while(l):
			#print l;
			print "From 1";
		client.close();

	s.shutdown(socket.shut_WR);
	s.close();

def Thread2():
	print("Starting Thread2")
	s2 = socket.socket();
	port2 = 12346;
	s2.bind(('10.0.0.5',port2));
	s2.listen(5);
	while True:
		client1, addr = s2.accept();
		print(" Got connection from" +  str(addr));
		#print " Receiving ";
		l2 = client1.recv(10)
		while(l2):
			#print l;
			print "From 2";
		client1.close();

	s2.shutdown(socket.shut_WR);
	s2.close();

try:
	a = threading.Thread(target=Thread1,);
	a.daemon = True;
	a.start();
	b = threading.Thread(target = Thread2,);
	b.daemon = True;
	b.start();
	while True: time.sleep(0.5)
	signal.signal(signal.SIGINT, sigint_handle);

except(KeyboardInterrupt,SystemExit):
	signal.signal(signal.SIGINT, sigint_handle);
	print "Error in starting threads";
	s2.shutdown(socket.shut_WR);
	s2.close();
	s.shutdown(socket.shut_WR);
	s.close();
