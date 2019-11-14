from scapy.all import PcapReader,Ether,IP
from itertools import islice
import csv

# 172.16.0.11 81.2.209.136 22252 5298 17
# src='172.16.0.11'
# dst='81.2.209.136'
# sport=1036
# dport=80
# proto=6
# packets=[]
subnet="172.16."

file = open("ISOT-172-16.csv","w")
writer = csv.writer(file,delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
writer.writerow(["src","dst","sport","dport","proto","time","len","macsrc","macdst"])
cnt = 0
total = 0
try:
    for pkt in PcapReader("ISOT_Botnet_DataSet_2010.pcap"):
        total += 1
        if IP in pkt and (pkt[IP].src[0:7]==subnet or pkt[IP].dst[0:7]==subnet):
            cnt += 1
            writer.writerow([pkt[IP].src,pkt[IP].dst,str(pkt[IP].sport),str(pkt[IP].dport),str(pkt[IP].proto),str(pkt.time),str(pkt[IP].len),pkt.src,pkt.dst])
            # pkt.show()
        if total%1000==0:
            print("\r", cnt, "/", total, total-cnt, end="")
        # pkt.show()
        # if pkt.haslayer('IP') and pkt[IP].proto==proto:
        #     cond1=pkt['IP'].src==src and pkt['IP'].dst==dst and pkt[IP].sport==sport and pkt[IP].dport==dport
        #     cond2=pkt['IP'].src==dst and pkt['IP'].dst==src and pkt[IP].sport==dport and pkt[IP].dport==sport
        #     if cond1 or cond2:
        #         packets.append(pkt)
    # print(len(packets))
except KeyboardInterrupt:
    pass 
finally:
    file.close()
