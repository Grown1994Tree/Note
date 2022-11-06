# 文件共享服务NFS.md

# 一、安装和启动
1. 安装指令 `yum install nfs-utils`

2. 启动与端口
    - 启动步骤：先启动RPC，再启动NFS。
        - 启动RPC：`systemctl start rpcbind` 端口为`111`
        - 启动NFS：`systemctl start nfs-server` 端口为`2049`
    - 由于NFS可能要调用多个端口，所以需要RPC进程的配合，在启动时会随机选择几个端口向RPC注册。
        - 通过`rpcinfo -p IP|localhost`指令来查看注册的端口信息
        ![avatar](/Linux/文件共享服务NFS/端口信息.png)

3. 配置信息
    - 配置文件为`/etc/exports` *<font size=2>exports文件不一定自带，可能需要手动建立</font>*
    - 配置方法详见下图。一个共享目录可以对应多个网段，网段之间使用空格分开，括号里面设置对应的操作权限
     ![avatar](/Linux/文件共享服务NFS/配置.png)
     ![avatar](/Linux/文件共享服务NFS/权限.png)
        - 权限问题：
            - 1. 除了挂载权限外，能进行什么样的操作取决于文件权限
            - 2. 文件用户组和用户取决于使用用户的uid和gid,如果uid和gid在服务器上存在对应的用户，则为该用户;如果挂载权限为匿名，则为nobody.
    - 重新挂载和卸载指令：`exportfs -[aruv]`
        - `-arv`: 重新挂载
        - `-auv`: 重新卸载

4. 查看可以挂载共享目录
    - 指令：`showmount -e IP|localhost`
     ![avatar](/Linux/文件共享服务NFS/查看共享目录.png)

5. 挂载：`mount -t nfs IP:目录 本地目录`
