# ssh

### 一、什么是ssh?
1. 一种加密的远程连接协议和工具，跟以往telnet和ftp的明文传输不同，对数据进行加密。
2.  保证了远程登录和远程通讯的安全，并支持多种登录验证模式。
     - 密码登录
     - 密钥登录
3. OpenSSH为开源免费，主流linux发行版都会默认安装。
4. ssh采用客户端-服务端模式，客户端实现为ssh,服务端实现为sshd

### 二、安装
1. 安装
通常系统都会自带安装ssh,如果没有按照以下命令行进行安装
` sudo apt-get install ssh `
安装完成既可以使用ssh命令。详细安装步骤见：https://www.cnblogs.com/linuxAndMcu/p/10766589.html#_label0
安装完成后就可以使用ssh加ip进行远程连接了。
`ssh 192.168.0.105`
但是没有设置登陆名，所以会以本机的用户作为登陆名来使用
2. 启动
正常的连接命令应该为
`ssh -l root 192.168.0.105`　或者　`ssh root@192.168.0.105`
输入密码就可以直接登陆了：
![avatar](/Linux/使用ssh和ftp功能/image/2021-06-23_04-24.png)

ssh命令的其他参数: https://www.linuxcool.com/ssh

### 三、密码登录
1. 登录流程
    -  第一次登录时，服务器会返回服务器的指纹，用来确认是否登录
    -  确认登录后，就会把服务器的指纹给保存到 ` ~/.ssh/known_hosts` 里面，下次登录时直接跳过该步骤。
    -  进入握手阶段，客户端提供支持的加密方法列表给服务端，服务端选择支持的方法后并返回给客户端
    -  服务端生成公钥和私钥，并暴露公钥给客户端。
    -  客户端使用公钥加密后发送给服务端。
    -  服务端使用私钥进行解密。
  ![avatar](/Linux/使用ssh和ftp功能/image/截图_2021-08-13_09-43-51.png)

2. 配置文件
   -  `~/.ssh/config` 通过该配置文件整合所有常用的远程登录模块，增加效率。
    ![avatar](/Linux/使用ssh和ftp功能/image/配置.png)
   - 其他配置字段参考：https://wangdoc.com/ssh/client.html#主要配置命令

3. 执行命令
两种方式：
    - 进入shell交互模式
    - 在`ssh`指令后面加上命令行执行语句`command`,但是无法进入shell交互模式
    ![avatar](/Linux/使用ssh和ftp功能/image/执行.png)

### 四、密钥登录
1. 登录流程
   -  客户端通过`ssh-keygen` 生成一组密钥，分别为私钥和公钥
   -  客户端把公钥上传到对应的服务器
   -  连接时，服务端使用客户端提供的公钥发送一些随机数据给客户，让客户证明身份
   -  客户端使用私钥对数据进行加密后（这个步骤叫做签名），发送加密数据到服务端
   -  服务端使用公钥解密后跟之前的数据进行对比，成功则通过验证。
  
2. 生成密钥
   -  使用 `ssh-keygen` 指令生成密钥，可以根据情况选择加密方式以及给私钥设置密码
      -  `-t [算法]`  可以设置密钥的生成算法
      -  `-N [密码]`  可以给私钥设置添加时间。
    ![avatar](/Linux/使用ssh和ftp功能/image/私钥.png)
    如上图所示，生成两个文件为id_rsa和id_rsa.pub,分别代表为私钥和公钥。
3. 上传公钥
  主要有两种方法：手动上传和自动上传
  - 手动上传
     OpenSSH规定，公钥保存在服务器用户目录文件夹的`~/.ssh/authorized_keys`文件里面，因此在本地使用指令串 `cat ~/.ssh/id_rsa.pub | ssh root@192.168.0.102 "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"  ` 进行执行。
![avatar](/Linux/使用ssh和ftp功能/image/服务器公钥.png) 
  - 自动上传
   方式一：使用OpenSSH自带的`ssh-copy-id`指令把公钥上传到指定的服务器,使用指令`ssh-copy-id -i ~/.ssh/id_dsa.pub root@192.168.0.102` 把传到服务器的`~/.ssh/authorized_keys`文件里面。
   <font size=2>由于`ssh-copy-id`指令会追加到文件的末尾，因此需要保证服务器公钥之间存在换行符，否则可能导致整个文件无法使用</font>*
   方式二：使用`scp`指令上传到服务器。`scp /home/sujingyang/.ssh/id_rsa.pub root@192.168.0.105:~/.ssh/authorized_keys` 
   *<font size=2>使用`scp`指令生成时可能会覆盖其他客户机的公钥，因此建议不要直接重命名为`authorized_keys`,而是上传后再追加</font>*
   ![avatar](/Linux/使用ssh和ftp功能/image/使用scp指令上传公钥.png) 
*

4. ssh-agent指令和ssh-add指令
- 目的：每次调用时，都会录入私钥的密码，通过使用ssh-agent指令和ssh-add指令可以避免每一次登录都要输入密码
- 使用：
  -  通过`eval ssh-agent`打开运行环境
  -  再使用`ssh-add`指令添加需要授予权限的私钥
![avatar](/Linux/使用ssh和ftp功能/image/ssh-add.png) 

5. 关闭掉密码登录
在服务端更改`/etc/ssh/sshd_config`文件的配置`PasswordAuthentication`属性为`no`后重启sshd服务

### 五、服务器模块
在SSH架构中，客户端运行的是ssh,服务端运行的是sshd
1. 启动sshd软件
   两种方式：`systemctl` 指令和运行可执行文件
   -  使用可执行文件`sshd` *<font size=2>使用sshd指令存在由于其他原因导致指向其他文件，所以最好使用`/usr/sbin/sshd`来执行</font>*
   -  使用 `systemctl enable sshd.service`来设置启动执行
  
2. 配置文件
   -  sshd 配置文件所在的目录为 `/etc/ssh`,主要的文件及含义如下图所示。
  ![avatar](/Linux/使用ssh和ftp功能/image/sshd主文件.png) 
   - 如果重装sshd软件可能导致客户端无法连接，因此在重装之前需要把`/etc/ssh`目录进行备份，重装完成后再进行覆盖
   -  常用指令：
      -  `sshd -f [文件]`  指定其他配置文件
      -  `sshd -t` 检查配置文件有没有语法错误
   - 如果对于配置文件有存在修改，需要重新启动服务
   -  sshd服务存在一些默认的文件，例如端口22。虽然该端口`port`使用`#`注释掉并不会影响使用，但是如果要更改为其他端口，则需要去掉`#`注释后再更改。 
![avatar](/Linux/使用ssh和ftp功能/image/port.png) 

### 六、端口转发(SSH隧道)



### 七、scp命令
1. 功能类似于`cp`指令，但是对密码和所传文件进行了加密。
2. 使用方法：`scp  [主机名：]sourcefile [主机名：]targetfile`,可以实现主机到本地、本地到主机以及主机之间的文件复制，如果主机名不填写，默认为在本地。
3. 常用配置项
   - `-C`  决定传递时是否压缩文件
   -  `-c`  决定加密方式
   -  `-l`   确定传输数据的带宽频率
   -  `-p`   保留文件的原始属性
   -  `-P`   指定端口

### 八、rsync指令
1. 功能：本地目录之间的同步；本地目录与远程主机之间的同步
2. 系统不一定会自带该软件，所以对于有的系统要使用`yum install rsync`进行安装。*<font size=2>通过`rsync -v`指令确认是否安装</font>*
3. 核心指令: `rsync -r [主机名：]source [主机名：]dest`
*<font size=2>在本地目录直接同步目录</font>*
![avatar](/Linux/使用ssh和ftp功能/image/rsync_本地.png) 
4. 核心配置项
   -  `-a`  跟`-r`一样对目录进行递归，但是会保留元文件的时间、权限等
  ![avatar](/Linux/使用ssh和ftp功能/image/rsync_同步信息.png) 
   -  `-n` 进行模拟执行，通常配合`-v`使用，展示出同步信息。
  ![avatar](/Linux/使用ssh和ftp功能/image/rsync_模拟.png)
  - `--delete` 确保目标目录作为源目录的副本，会删除掉目标中不存在源目录的文件。该过程无法通过`-n`进行模拟
![avatar](/Linux/使用ssh和ftp功能/image/rsync_delete.png)
  - `--exclude`   排除文件
    三种模式：
      -  使用 `--exclude 文件名或通配符`
      -  使用 `--exclude={文件名或通配符，文件名或通配符}`
      -  使用 `--exclude-from="配置文件"`，把要排除的写道配置文件里
      - `--include`   指定要同步的文件的文件，通常跟`--exclude`使用。
5.  远程同步目录到服务器
![avatar](/Linux/使用ssh和ftp功能/image/rsync_远程.png) 
*<font size=2>需要使用`-e`配置项来指定所用协议</font>*

6. 增量备份
-  增量备份概念：第一次备份为全库备份，以后每次只对有改变的数据进行备份。
-  常用配置项：`--list-dest [基准目录]`  指向同步时的基准目录



### 九、sftp命令
相比于`ftp`命令，`sftp`命令会对上传的文件进行加密，其他指令跟使用ftp相同。
