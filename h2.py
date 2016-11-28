import socket
import thread
import time
def rec_pmu(s):
 data_list = [];
 while True :
	client , addr = s.accept();
	print("Got connection from" + str(addr));
	print "Receiving...";
	l = client.recv(30)
	while (l):
		print "Receiving...";
		data_list.append(l)
		l = client.recv(30);
		if(len(data_list) == 100):
			send_oa(data_list);
			del data_list[:];
	#f.close();
	print "Done Receiving";
	client.close();
	break;
def send_oa(data_list):
 while True:
	ss.send(str(data_list));
s = socket.socket();
host = socket.gethostname();
port = 12345;
print(host);
s.bind (('10.0.0.2',port));
#f = open('pmu_data_recv.txt', 'wb');
s.listen(5);
while 1:
	ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
	try:
		ss.connect(('10.0.0.5',12346));
		rec_pmu(s)
	except:
		print("Sleeping briefly");
		time.sleep(5)
		continue

s.shutdown(socket.SHUT_WR);
s.close();
ss.shutdown(socket.SHUT_WR);
ss.close(socket.SHUT_WR);
