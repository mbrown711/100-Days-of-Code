# blocking out potentially sensitive information with ***
ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500 #if wired, ethernet connection
        inet ***  netmask ***  broadcast ***
        inet6 ***  prefixlen *** scopeid ***
        inet6 ***  prefixlen ***  scopeid ***
        inet6 ***  prefixlen ***  scopeid ***
        ether ***  txqueuelen ***  (Ethernet)
        RX packets ***  bytes *** (***)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets ***  bytes *** (***)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=***<UP,LOOPBACK,RUNNING>  mtu *** # localhost
        inet 127.0.0.1  netmask ***
        inet6 *** prefixlen ***  scopeid ***
        loop  ***  (Local Loopback)
        RX packets ***  bytes *** (***)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets ***  bytes *** (***)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

# changing IP address with ifconfig:
ifconfig eth0 192.***.***.***

# changing network mask and broadcast address:
ifconfig eth0 192.***.***.*** netmask 255.***.***.*** broadcast 192.***.***.***

# changing media access control (MAC) address with ifconfig:

ifconfig eth0 down
ifconfig eth0 hw ether 00:11:22:33:44:55
ifconfig eth0 up

# changing DHCP client without having to shut down
# request an IP address from DHCP, call the DHCP server followed by an interface to the address you want:
dhclient eth0

# examining DNS with dig
dig hackers-arise.com ns # ns is name server
dig hackers-arise.com mx # mx is mail exchange server

# changing your dns server - need to open in a text editor like so:
leafpad /etc/resolv.conf
echo "nameserver 8.8.8.8"> /etc/resolv.conf # address is google's public domain
leafpad /etc/resolv.conf

