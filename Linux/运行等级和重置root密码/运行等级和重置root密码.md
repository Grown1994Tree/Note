#运行等级和重置root密码

###一、运行级别
linux的运行级别主要有6个级别，其中比较常用的级别为3和5。
- 0 系统停机魔石，系统默认运行级别不能设置为0，否则不能正常启动
- 1 单用户模式，root权限，用于系统维护，禁止远程登录，就像Windows下的安全模式登录
- 2 多用户模式，没有NFS和网络支持
- 3 完整的多用户文本模式，有NFS和网络，登录后进入控制台命令行模式
- 4 系统未使用，保留一般不用，在一些特殊情况下可以用它来做一些事情。例如在笔记本电脑的电池用尽时，可以切换到这个模式来做一些设置
- 5 图形化模式，登录后进入图形GUI模式，X Windows系
- 6 重启模式，默认运行级别不能设置为6，否则不能正常启动。运行init 6机器就会重启。

常用命令行
1. 获取现在的运行等级 `runlevel`
结果：可以获取经历过的运行级别，第一个为上一次，第二个为这一次。
![avatar](/Linux/运行等级和重置root密码/runlevel.png)

2. 切换运行级别 `init [0-6]`，输入认证密码后既可以切换  *<font size=1>[0-6]所代表的含义见上面</font>*

3. 使用 `init` 命令行可以切换运行级别，但是只是暂时使用,重启后就会变为默认的运行等级。所以需要使用`systemctl get-default` 和 `systemctl set-default` 两个命令行进行设置。
   - `systemctl get-default` 查看现在的默认运行级别
      ![avatar](/Linux/运行等级和重置root密码/graphical.png)
   - `systemctl set-default [运行级别]`  设置默认运行级别
      ![avatar](/Linux/运行等级和重置root密码/multi-user.png)
   
###重设root用户的密码
主要分为以下几个步骤：
1. 重新启动系统后，进入grub页面，按住e键编辑grub的参数。
2. 把 `ro` 以及后面所有文字换成 `rw init=/bin/sh`。
3. 使用 `passwd` 命令行修改root密码
4. 执行 `exec /sbin/init` 命令行