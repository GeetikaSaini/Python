import socket
host=input("Enter the ip address or domain name you want to scan:")
print("Enter the range of port you want to scan:")
start_port=int(input("Enter the starting port:"))
stop_port=int(input("Enter the last port:"))
try:
    ip=socket.gethostbyname(host)
    print(ip)
except socket.gaierror:
    ip = host
    print(f"Using IP directly: {ip}")
else:
    ip=host
print(f"Port  | status | Service")
for i in range(start_port,stop_port+1):
    scan_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    scan_socket.settimeout(1)
    result=scan_socket.connect_ex((ip,i))
    try:
        service = socket.getservbyport(i)
    except OSError:
        service = "unknown"
    if result==0:
        status='OPEN'
    else:
        status='CLOSED'
    
    print(f"{i:<5} | {status:<6} | {service}")

