#!/bin/bash
echo "Enter the network address you want to scan (192.168.0.):"
read network_addr
for ip in {1..254}
do
    addr="$network_addr.$ip"
    echo "Scanning $addr"
    ping -c 1 -W 1 $addr > /dev/null 2>&1
    if [ $? -eq 0 ]
    then
         echo " -> $addr is alive"
    fi
done

