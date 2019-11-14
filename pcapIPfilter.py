from scapy.all import PcapReader, IP, PcapWriter
from itertools import islice
import sys
ips = ["172.16.2.11",
"172.16.0.2",
"172.16.0.12",
"172.16.2.2",
"172.16.2.3",
"172.16.2.11",
"172.16.2.12",
"172.16.2.13",
"172.16.2.14",
"172.16.2.111",
"172.16.2.112",
"172.16.2.113",
"172.16.2.114",
"172.16.0.11"]

pktdumps = { ip : PcapWriter(ip+".pcap", append=False, sync=True) for ip in ips }

cnt = 0
total = 0
try:
    for pkt in PcapReader("172-16-subnet.pcap"):
        total += 1
        
        if IP in pkt and pkt[IP].src in pktdumps:
            pktdumps[pkt[IP].src].write(pkt)
            cnt += 1
            # print("\r", cnt, "/", total, total-cnt, end="")
        if IP in pkt and pkt[IP].dst in pktdumps:
            pktdumps[pkt[IP].dst].write(pkt)
            cnt += 1
            # print("\r", cnt, "/", total, total-cnt, end="")
        if total%10000==0:
            print("\r", cnt, "/", total, total-cnt, end="")

except KeyboardInterrupt:
    pass
finally:
    for ip in ips:
        pktdumps[ip].close()
print("done")
