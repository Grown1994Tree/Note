### 一、NMAP步骤

```shell
1. 目标枚举
2. 主机存活探测
3. DNS反向查询
4. 端口扫描
5. 版本探测
6. 操作系统探测
```

### 二、目标枚举

```shell
# 四种方式:
1. nmap [域名|IP] [域名|IP] [域名|IP] ....
2. nmap [IP范围] # 例如：10.10.11.2-20、10.10.11-25.12-25
3. nmap [子网] # 例如 10.10.11.2/24
4. nmap -iL [文件名] 
### 对于列表也可以使用-sL参数，该参数会反向获取IP的DNS信息，添加-n参数可以禁止DNS查询
```

### 三、探测主机存活情况

```shell
# 三种方式
1. 同个子网：nmap -PR -sn TARGETS # 使用ARP协议进行扫描
2. 不同子网：nmap -PE -sn TARGETS # 使用ICMP的ping来探测
3. TCP/UDP: 
    3.1 nmap -PS -sn TARGETS # SYC扫描，管理员权限为半连接，非管理员权限为全连接
    3.2 nmap -PA -sn TARGETS # ACK扫描，有回复则为在线
    3.3 nmap -PU -sn TARGETS # UDP扫描，没有回复则为在线
    ### TCP/UDP方式需要使用超级管理员权限，否则都会导致完成三次握手，从而留下日志。
    ### 默认使用常用的80端口和443端口，可以在-PS/-PA/-PU后续明确指定端口 
```

### 四、DNS反向查询

```shell
1. 禁止反向查询：nmap -n -sn TARGETS
2. 强制反向查询：nmap -R -sn TARGETS --dns-servers DNS_SERVER # 指定dns服务器
### 通常配合主机存活探测使用
```

### 五、端口扫描

1. 端口服务状况

```shell
1. Open:开放
2. Closed:关闭
3. Filtered:防火墙阻碍，无法确认服务开通或关闭
4. Unfiltered:防火墙没有阻碍，无法确认服务开通或关闭，通常用于-sA扫描的结果
5. Open|Filtered:无法确认打开或被阻碍
6. Closed|Filtered：无法确认关闭或被阻碍
```

2. 普通扫描

```shell
# 三种方法
1. nmap -sT TARGET # 全连接扫描，完成三次握手，因此会留下日志
2. nmap -sS TARGET 
# 半连接扫描，没有完成三次握手，但是不会留下日志，默认扫描方式
# 没有使用超级管理员权限也会完成三次握手。
3. nmap -sU TARGET # UDP扫描，开放端口不会回复
```

3. 隐蔽扫描

```shell
# 三种方法
1. nmap -sN TARGET # 数据包不设置数据包标志
2. nmap -sF TARGET # 数据包设置FIN标志
3. nmap -sX TARGET # 数据包设置FIN\PSH\URG标志
### 三种扫描方式都是返回RST,ACK认定为关闭，否则为无法确认打开或被阻碍
### 
```

4. 探测防火墙规则

```shell
1. nmap -sA TARGET # 数据包设置ACK标志
### 
```

### 六、版本探测

```shell
### 探测目标端口对应的服务版本
nmap -sV TARGET
# 参数
# --version-intensity LEVEL #LEVEL范围0-9，数值越大越详细
### 该方案一定会完成三次握手，不能跟-sS公用，因此会留下记录
```

### 七、操作系统探测

```shell
### 探测目标端口对应的操作系统版本
nmap -sO TARGET
### 可以跟-sS使用，但是结果不是很精确，特别是由于虚拟化的存在
```

### 八、常用参数

1. 指定端口

```shell
# 例如：
# 指定端口列表：-p22,80,443,扫描22、80和443三个端口
# 指定端口范围: -p1-1023
# 所有端口: -p-
# 指定最常用的前100个端口: -F
# 指定前几个常用端口: --top-ports num
# 端口扫描顺序: -r,该端口可以按照指定顺序扫描
```

2. 扫描速率

```shell
# 例如：
# -T <number>：设置等待时间，参数通常为1-5，数值越大，等待时间越短，但是准确率越低，默认为-T 3,实战中建议为-T 1
# --min-rate <number>: 设置最小速率
# --max-rate <number>：设置最高速率
# --min-parallelism <numprobes>: 设置最小并发数 
# --max-parallelism <numprobes>：设置最大并发数
```
