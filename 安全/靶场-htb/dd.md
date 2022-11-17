SMC软件-HTTPS  6789端口

https://10.129.150.132:8443/manage/account/login?redirect=%2Fmanage

https://10.129.150.132:8443/manage/account/login?redirect=/etc/passwd


Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-17 18:59 CST
Nmap scan report for 10.129.150.132
Host is up (7.1s latency).
Not shown: 595 closed tcp ports (reset), 402 filtered tcp ports (no-response)
PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
6789/tcp open  tcpwrapped
8080/tcp open  tcpwrapped
Device type: firewall
Running (JUST GUESSING): Fortinet embedded (87%)
OS CPE: cpe:/h:fortinet:fortigate_100d
Aggressive OS guesses: Fortinet FortiGate 100D firewall (87%)
No exact OS matches for host (test conditions non-ideal).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 3389/tcp)
HOP RTT    ADDRESS
1   ... 30

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 483.06 seconds

重定向端口8443