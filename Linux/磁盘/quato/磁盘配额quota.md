# 磁盘配额quota

### 一、为什么要有磁盘配额
1. 目的：linux是多用户操作系统，为了更方便每个用户或组的操作，需要对每个用户或组占据的目录资源进行管理。简而言之，需要更多资源的用户拥有更多的资源。
2.  管理：所谓的管理指的是对用户或者组进行inode数量和block容量的管理
    -  对inode数量进行管理 *<font size=2>存放文件的元信息，一个文件对应一个inode节点</font>*
    -  对磁盘块block进行管理 *<font size=2>块由多个扇区组成</font>*
    -  当容量已经超过设定时，会先对用户进行警告，如果还未处理将直接失去新增权限
3. 主要指令：setquota、quotaon、quotaoff、edquota

### 二、主要步骤
1. 检验文件系统是否符合quota的使用要求
   -   判断是否为单独的文件系统，quota只能单个分区进行管理，通常使用`df -h`指令
     ![avatar](/Linux/磁盘/quato/判断是否为单独分区.png)
   -   判断该文件系统是否支持对用户或者组配额的支持，也就是说该文件系统是否支持`usrquota`或者`grpquota`权限，如果不支持则进行添加，
        -  使用`cat /etc/fvstab`来查看用户是否拥有该权限，如果没有直接添加权限后重启
     ![avatar](/Linux/磁盘/quato/配额权限.png)
        -  使用`mount | grep home` 来查看是否拥有该权限，否则使用`mount -o remount,usrquota,grpquota /home` 添加权限，短暂增加，无须重启系统。
      ![avatar](/Linux/磁盘/quato/权限.png)
2. 用户配额
        -  获取记录表，核心指令为`quotacheck`,该指令只对支持quota的文件系统进行扫描，并创建`aquota.group`文件或者`aquota.user`文件。
      ![avatar](/Linux/磁盘/quato/quotacheck_au.png)
      ![avatar](/Linux/磁盘/quato/quotacheck_au1.png)
      *<font size=2>这两个文件无法直接编辑</font>*
      -  启动和关闭quota
         -  开启quota:两个常用指令
            -  `quotaon -augv`:对所有挂载点启动。
               -  `-a` 表示针对所有挂载点启动。
               -  `-u` 表示对用户启动磁盘配额
               -  `-g` 表示对组启动磁盘配额
               -  `-v` 展示启动过程的相关信息
            -  `quotaon -uv [挂载点]`：针对某些挂载点的用户或者组进行挂载
         -  关闭quota指令：`quotaoff`
    ![avatar](/Linux/磁盘/quato/启动和关闭quota功能.png)
      -  编辑磁盘配置和临界时间，两种方案
         -  方案一：
            -  核心指令为使用`edquota -u [username] -g [groupname]`指令去设置磁盘配额。
            -  `edquota -p [username] [username]` 复制磁盘配额范本到其他用户
            -  `edquota -t ` 设置限定时间。
          ![avatar](/Linux/磁盘/quato/3配置quota信息.png)
         -  方案二：使用`setquota [-u|-g] [username | groupname ] block(soft) block(hard) inode(soft) inode(hard) 文件系统`命令行直接增加配额，可以方便的在shell里面配合创建用户使用。
      -  打印报表
         - 针对单用户`quota -[ugvs] [username | groupname ] `
         - 针对所有用户：`repquota -[augsv]`
        ![avatar](/Linux/磁盘/quato/4查看quato报表.png)

3. 定期检查
    - warnquota的安装:使用`yum install quota-warnquota`指令额外安装后才能使用
    - 在`/etc/warnquota`路径配置邮件相关信息
