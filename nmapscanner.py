import nmap
scanner = nmap.PortScanner()
ip_addr=int(input("Please enter the Ip address you want to scan: "))
print("The IP you entered us: ",ip_addr)
resp=input("""\nPlease enter the type of scan you want to run
           1)SYN ACK Scan
           2)UDP Scan
           3)Comprehensive Scan""")
print('You have selected option: ',resp)
if resp =='1' :
    print('Nmap Version: ',scanner.nmap_version())
    scanner.scan(ip_addr,'1-1024','-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ",scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp =='2' :
    print('Nmap Version: ',scanner.nmap_version())
    scanner.scan(ip_addr,'1-1024','-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ",scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
else:
    print('Nmap Version: ',scanner.nmap_version())
    scanner.scan(ip_addr,'1-1024','-v -A')
    print(scanner.scaninfo())
    print("Ip Status: ",scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
