from scapy.all import *

conf.verb = 0

p = IP(dst="192.168.32.0/24")/TCP(dport=80,flags="S")
ans, unans= sr(p,timeout=3)

for a in ans:
    if a[1].flags == 2:
        print(a[1].src+"\r\n")