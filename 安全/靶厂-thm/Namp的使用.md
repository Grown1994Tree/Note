### 一、探测主机是否上线

1. 利用ARP协议验证端口

### 探测主机是否上线

# 四种方式
ARP from Link Layer
ICMP from Network Layer
TCP from Transport Layer
UDP from Transport Layer

# 使用arp
nmap -PR -sn TARGETS

sudo arp-scan -I eth0 -l

# 使用ping
nmap -PE -sn MACHINE_IP/24

# 时间戳
nmap -PP -sn MACHINE_IP/24

# mask
nmap -PM -sn MACHINE_IP/24

# tcp syn包
nmap -PS -sn MACHINE_IP/24

# tcp ack包
nmap -PA -sn MACHINE_IP/24

Scan Type	Example Command
ARP Scan	                          sudo nmap -PR -sn MACHINE_IP/24
ICMP Echo Scan	                 sudo nmap -PE -sn MACHINE_IP/24
ICMP Timestamp Scan	         sudo nmap -PP -sn MACHINE_IP/24
ICMP Address Mask Scan	   sudo nmap -PM -sn MACHINE_IP/24
TCP SYN Ping Scan	          sudo nmap -PS22,80,443 -sn MACHINE_IP/30
TCP ACK Ping Scan	         sudo nmap -PA22,80,443 -sn MACHINE_IP/30
UDP Ping Scan	                 sudo nmap -PU53,161,162 -sn MACHINE_IP/30