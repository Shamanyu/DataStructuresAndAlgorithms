import socket
import re
from struct import *
s=socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
while True:
	packet=s.recvfrom(65565)
	packet=packet[0]
	ip_header=packet[0:20]
	iph=unpack('!BBHHHBBH4s4s', ip_header)
	version_ihl=iph[0]
	version=version_ihl>>4
	ihl=version_ihl&0xF
	ttl=iph[5]
	protocol=iph[6]
	s_addr=socket.inet_ntoa(iph[8])
	d_addr=socket.inet_ntoa(iph[9])
	print 'Version: '+str(version)+' IP HEADER Length: '+str(ihl)+' TTL: '+str(ttl)+' Protocol: '+str(protocol)+' Source Address: '+str(s_addr)+' Destination Address: '+str(d_addr)
	tcp_header=packet[20:40]
	tcph=unpack('!HHLLBBHHH', tcp_header)
	source_port=tcph[0]
	dest_port=tcph[1]
	sequence=tcph[2]
	acknowledgment=tcph[3]
	doff_reserved=tcph[4]
	tcph_length=doff_reserved>>4
	print 'Source Port: '+str(source_port)+' Dest Port: '+str(dest_port)+' Sequence Number: '+str(sequence)+' Acknowledgment: '+str(acknowledgment)+' TCP Header length: '+str(tcph_length)
	h_size=ihl*4+tcph_length*4
	data_size=len(packet)-h_size
	data=packet[data_size:]
	message_header="gotMessage"
	print 'Data: '+str(data)
	target=open("Messages.txt", 'a+')
	if(str(data).find(message_header) != -1):
		start=str(data).find('["gotMessage",')+15
		end=str(data).find('"]')
		target.write(str(data[start:end]))
		target.write('\n')
	
