import socket
import thread
import time
import json
def rec_pmu(s):
 data_list = [];
 while True :
	client , addr = s.accept();
	print("Got connection from" + str(addr));
	print "Receiving...";
	l = client.recv(1024)
	while (l):
		print "Receiving...";
		data_list.append(l)
		l = client.recv(1024);
		if(l):
			print l;
			send_oa(data_list);
			del data_list[:];
			#send_oa(l)
	#f.close();
	print "Done Receiving";
	client.close();
	break;
def send_oa(data_list):

 while True:
	#data_list = json.dump(data_list,ensure_ascii = False)
	ss.send(str(data_list));
s = socket.socket();
host = socket.gethostname();
port = 12399;
print(host);
s.bind (('10.0.0.1',port));
#f = open('pmu_data_recv.txt', 'wb');
s.listen(5);
ss = socket.socket();
host1 = socket.gethostname();

ss.connect(('10.0.0.5',12345));
rec_pmu(s);

s.shutdown(socket.SHUT_WR);
s.close();
ss.shutdown(socket.SHUT_WR);
ss.close();
