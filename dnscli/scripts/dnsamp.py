from scapy.all import *
import time

# IP address of the DNS client from which the query is sent
source_ip = '10.0.0.2'  # Replace with the actual IP of one of your DNS clients

# IP address of the Pi-hole server
target = '10.0.0.5'  # Replace with your Pi-hole server IP

# DNS Query to Pi-hole server
for i in range(10):
    packet = IP(src=source_ip, dst=target)/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname='globo.com', qtype='ANY'))
    time.sleep(1)


    # Send the packet
    send(packet)

