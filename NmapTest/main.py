import nmap

targetHost = "192.168.137.10"
nmScan = nmap.PortScanner('C:\\Program Files (x86)\\Nmap\\nmap.exe')
nm=nmScan.scan(targetHost,'22-80')
print(nm)