# samba文件共享服务器

### 一、概念和主要文件  

1. NetBIOS 通讯协议，局域网中的通信协议
2. SAMBA常用服务

- nmbd：管理工作组、NetBIOS 通讯协议的用户，主要端口为137、138，利用 UDP 协议
- smbd：管理共享文件，目录以及打印机和权限管理，主要端口为139、445，利用TCP协议

3. 需要安装的软件

- 服务端 samba（nmbd、smbd程序）samba-common（主要配置文件）
- 客户端 samba（工具指令）samba-common（主要配置文件）

4. 主要文件。

- /etc/samba/smb.conf  Samba 的主要配置文件，主要设置全局（global）参数和共享资源
- /etc/sysconfig/samba 服务运行时所需的参数
- /etc/samba/smbusers 管理window和linux之间账号的关系
- /var/lib/samba/private/{passdb.tdb,secrets.tdb} 管理 Samba 的用户账号/密码

5. 运行程序和脚本
服务器

- /usr/sbin/{smbd,nmbd}  权限管理 (smbd) 以及 NetBIOS name 查询 (nmbd)
- /usr/bin/{tdbdump,tdbtool} 管理账号数据，需要安装tdb-tool。tdbdump 可以察看数据库的内容，tdbtool 则可以进入数据库操作接口直接手动修改帐密参数
- /usr/bin/smbstatus 联机信息
- /usr/bin/{smbpasswd,pdbedit} 管理用户数据  和/usr/bin/{tdbdump,tdbtool} 有什么区别
- /usr/bin/testparm  检验/etc/samba/smb.conf 语法是否正确
客户端
- /sbin/mount.cifs 挂载目录到本地
- /usr/bin/smbclient 查看和登录共享出来的目录，操作类似于ftp
- /usr/bin/nmblookup 查看NetBIOS 通讯协议的用户
- /usr/bin/smbtree 类似于网上邻居

### 二、服务器运行

1. 进入配置文件`/etc/samba/smb.conf`修改samba服务的参数及共享路径
![avatar](/Linux/SAMBA/配置文件.png)

主要模块为配置模块[global]和其他共享目录模块
配置模块用来设置工作组、配置安全模式
共享目录模块用来配置共享目录，模块名称会映射到目录，可以配置权限和是否使用selinux

使用`testparm` 指令验证是否配置正确

2. 建立目录及用户
注意：
    - 对目录的访问权限是仍然需要根据UID和GID来进行判断
    - 外部用户对共享目录的访问是以工作组的形似进行访问，因此操作取决于用户组的权限
综上所述，需要在本地（/etc/passwd）建立起对应的用户。
具体操作：
    - 建立用户组及对应的用户
    - 调整目录对应的`rwx`权限
    - 使用`pdbedit`对samba帐户进行管理，建立对应的账户
至此，我们就可以从客户端进行访问

### 三、客户端

主要有两种使用方式

1. 使用`smbclient`指令登陆，具体操作跟`ftp`工具差不多
2. 使用`mount -t cifs` 进行挂载
