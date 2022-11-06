# NIS服务器搭建

### 概述：NIS服务器用来管理局域网内各个主机的账户信息，需要跟RPC合作使用
![avatar](/Linux/NIS服务器搭建/管理内容.png)

### 一、应用程序安装
1. 服务端：
    - 使用`yum -y install yp-tools ypserv`进行安装

2. 客户端：
    - 使用`yum -y install yp-tools ypbind`进行安装

由于NIS服务需要RPC服务的支持，因此也需要使用`yum -y install rpcbind`来安装该服务。

### 二、服务端配置
`/etc/ypserv.conf`文件：筛选可以使用NIS服务的网段和主机
`/etc/hosts` : 配置主机IP和主机信息
![avatar](/Linux/NIS服务器搭建/网络配置.png)
`/etc/sysconfig/network`: 配置网络信息

### 三、启动服务
分为两个步骤：启动`ypserv`、`yppasswdd`服务以及创建NIS数据库
    - 启动服务：
        `systemctl start ypserv` 该服务启动后NIS服务器才能运行
        `systemctl start yppasswdd` 提供用户对秘密修改的权限
    - 创建NIS数据库（要先建立用户）
        `/usr/lib64/yp/ypinit -m` 通过该指令创建NIS用户数据库

### 四、客户端配置和测试
使用`setup`指令进入快捷配置工具，需要使用`yum -y install setuptool`对工具进行安装.
![avatar](/Linux/NIS服务器搭建/连接NIS服务.png)

连接正常后可以使用`yptest`指令进行测试或者使用`su - 用户`登陆

### 五、使用autofs自动挂载NFS文件共享服务
1. 安装指令：`yum -y install autofs`
2. 主要配置文件：
    - `/etc/auto.master`: 主映射文件，用来设置对挂载点挂载文件系统。
    - `/etc/auto.*`: 主映射文件挂载的文件系统，在里面设置文件目录及权限。
    - `/etc/sysconfig/autofs` : 配置autofs的各种设置
    ![avatar](/Linux/NIS服务器搭建/挂载.png)
3. 启动： `systemctl start autofs`
  