# 手动设置网络IP

### 一、临时设置
1. 使用`ifconfig [网卡名] [IP] netmask [子网掩码]`临时设置服务器IP ，重新设置后可以直接访问。
   ![avatar](/计算机网络/ifconfig临时设置IP.png)
2. 当服务器重启后，无法登录，可以断定通过`ifconfig`指令设置的IP地址是临时使用
![avatar](/计算机网络/ifconfig临时设置IP.png)
3. 使用`ifconfig [网络卡号] {up|down}` 可以对网络卡号进行开始和关闭
4. 通过`ifconfig [网络卡号：编号] IP`可以给当个卡号设置多个IP

### 二、长久设置
1. 在Red Hat中，进入`/etc/sysconfig/network-scripts/ifcfg-enp0s3 `文件进行修改
主要参数如下图所示：
![avatar](/计算机网络/配置参数.png)

2. 通过修改`BOOTPROTO`的值来修改获取IP的方式。如果要手动修改IP，则修改值为`none`；如果要自动获取IP，则值改为`dhcp`

3. 输入对应的IP（IPADDR）和子网掩码（NETWORK）后重新启动网络就配置成功。

4. 修改完成后可以通过`ifup [网络卡号]`和`ifdown [网络卡号]`对网络进行设置。*<font size=2>如果已经使用`ifconfig [网络卡号]`指令进行设置，无法使用`ifdown`进行关闭，需要使用`ifconfig [网络卡号] down` </font>*

其他参数详见图片配置参数

![avatar](/计算机网络/需要注意的配置文件.png)

*<font size=2>除了`ifconfig`,也可以使用`ip addr`指令来查看IP</font>*

### 三、IP指令
1. `ip`指令集合了`ifconfig`、`ifup`、`ifdown`和`route`几个指令的功能，同时还有其他更为强大的功能
2. `ip`指令主要分为三个部分：`link`、`address`、`route`
3. `link`的使用
   -  查看网卡的接口信息
  ![avatar](/计算机网络/查看网卡硬件信息.png)
   - 关闭和打开网卡，相当于`ifup`和`ifdown`的功能
    ![avatar](/计算机网络/关闭和打开网卡.png)
   - 修改网卡名称，修改之前需要先关闭网卡。如果网卡的MAC地址允许修改，可以使用`address`选项直接修改
  ![avatar](/计算机网络/修改网卡的名称.png)
4. `address`的使用：查看、修改以及增减IP地址
   - 使用`ip addr/address show`可以查看IP信息
   ![avatar](/计算机网络/查看IP信息.png)
   - 使用`ip addr/address {add|del}`
![avatar](/计算机网络/增加和删除IP地址.png)

### 四、命令行使用dhcp
使用`dhclient [网卡名]`命令行直接打开

### 五、网路侦测
1. `ping`指令：来确定两个网络之间的连接是否顺畅
   - 常用选项：
     - `-c [数值]`：确定ping的次数。*<font size=2>跟window不同，linux没有次数限制，需要使用`-c`来确定次数</font>* 
     - `-M {do|dont}`:是否允许其他主机分包,体现在时间上的差别，通过跟`-s`选项配合来确认ICMP分包的大小
  ![avatar](/计算机网络/是否允许分包.png)
  ![avatar](/计算机网络/确认分包.png)
      - `-n`：在输出数据时不进行 IP 与主机名的反查，直接使用 IP 输出(速度较快)；
      - `-s` 数值：发送出去的 ICMP 封包大小，预设为 56bytes，不过你可以放大此一数值；
       - `-t` 数值：TTL 的数值，预设是 255，每经过一个节点就会少一；
       - `-W` 数值：等待响应对方主机的秒数。
2. `traceroute [ip]`:会检测到目标IP所遇到的各个节点进行检测
  ![avatar](/计算机网络/traceroute.png)
   ![avatar](/计算机网络/traceroute常用选项.png)

3. `netstat`指令：
![avatar](/计算机网络/netstat用法.png)
两种用法：
   - `netstat -rn`：获取路由表  
   - `netstat -an`：获取服务以及端口
![avatar](/计算机网络/netstat字段.png)



