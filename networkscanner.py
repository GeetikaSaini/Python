import nmap

nm = nmap.PortScanner()

subnet = input("Enter the subnet you want to scan (e.g. 192.168.1.0): ")

net = subnet.split('.')
network = net[0] + '.' + net[1] + '.' + net[2] + '.'

start = 1
end = 255

print("\nScanning network...\n")

for ip in range(start, end):
    addr = network + str(ip)

    try:
        nm.scan(hosts=addr, arguments='-sn')

        if nm[addr].state() == "up":
            print(addr, "is alive")

    except KeyError:
        pass
