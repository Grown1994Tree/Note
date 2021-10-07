##简述使用ssh和ftp功能

### 一、使用ssh进行远程连接
##### 1、安装
通常系统都会自带安装ssh,如果没有按照以下命令行进行安装
` sudo apt-get install ssh `
安装完成既可以使用ssh命令。详细安装步骤见：https://www.cnblogs.com/linuxAndMcu/p/10766589.html#_label0
安装完成后就可以使用ssh加ip进行远程连接了。
`ssh 192.168.0.105`
但是没有设置登陆名，所以会以本机的用户作为登陆名来使用
#####2、启动
正常的连接命令应该为
`ssh -l root 192.168.0.105`　或者　`ssh root@192.168.0.105`
输入密码就可以直接登陆了：
![avatar](/Linux/使用ssh和ftp功能/image/2021-06-23_04-24.png)

ssh命令的其他参数:https://www.linuxcool.com/ssh

## 二、安装ftp服务站
##### 1、安装vsftpd
使用`rpm -qa|grep vsftpd`命令行查看软件是否安装vsftpd
如果还未安装，使用`yum install vsftpd`进行安装

##### 2、启动
使用命令行 `vim /etc/vsftpd/vsftpd.conf` 对ftp进行配置
![avatar](/Linux/使用ssh和ftp功能/image/2021-06-23_04-44.png)

配置完成后,需要使用下列命令行打开服务
`systemctl start vsftpd`
`systemctl enable vsftpd`

因为防火墙还开着所以,所以会提示无法访问主机
![avatar](/Linux/使用ssh和ftp功能/image/2021-06-23_05-27.png)
因此，需要执行一些命令行就可以关闭防火墙
`systemctl stop firewalld.service`

这样就可以直接访问ftp服务器了。
![avatar](/Linux/使用ssh和ftp功能/image/2021-06-23_05-30.png)

使用匿名用户anonymous就可以不需要密码直接登陆
![avatar](/Linux/使用ssh和ftp功能/image/2021-06-23_05-35.png)

##### 3、操作指令
  - 操作客户机目录
    - `!ls` 通过该指令查看本地目录的文件
    - `lcd [目录] ` 切换到客户机路径*<font size=2>上传或下载的终端<font>*
    - `put 文件名 [重命名]` 从客户机上传文件到服务器，支持重命名
    - `mput 文件名 [文件名]` 从客户机直接上传多个文件到服务器 
  
  - 操作服务器目录
    - `get 文件名 [重命名]` 从服务器下载文件到客户机，支持重命名
    - `mget 文件名 [文件名]` 从服务器直接下载多个文件到客户机
  
##### 4、允许root用户登陆
  1. 进入`etc/vsftpd`目录
  2. 修改`ftpuser`和`user_list`文件，去除root用户