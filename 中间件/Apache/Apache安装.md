# Apache安装与配置
# 环境centOs7

# 一、主要软件模块
主要软件：`yum install httpd mysql mysql-server php php-mysql`

# 二、apache主要目录
1. 主要配置文件：`/etc/httpd/conf/httpd.conf`

2. 次要配置文件：`/etc/httpd/conf.d/*.conf` `/etc/httpd/conf.d/`目录存在一些以conf后缀的配置文件，会被引入主配置文件

3. 模块目录：`/etc/httpd/modules/`路径为`/usr/lib64/httpd/modules/`的软链接

4. 默认资源目录：`/var/www/html/` 可以在主配置文件中的`DocumentRoot`选项进行自定义配置。

5. 日志文件:`/etc/httpd/logs`  为`var/log/httpd`路径在`httpd`配置文件夹的软链接。主要有`access.log`和`error.log`两个文件。

# 三、配置文件常用指令
Apache:
1. `<IfDefine [!]param >....</IfDefine>` 在服务执行时，通过参数启动对应模块。如果该指令里面嵌套多个IfDefine指令，则为使用多个参数。

2. `<IfModule [!]module >....</IfModule>` 当对应模块加载完成后，启动对应的模块。

3. `<Directory [~ 正则|路径]>....</Directory>` 用来对目录进行设置，设定访问权限、cgi程序等。
同理：`<File [~ 正则|文件名]>....</File>` 用来对文件进行限定
```
<Directory /usr/share/httpd/noindex>
    Options Indexes   #目录设定，即针对Apache程序对该目录权限的设定
    AllowOverride none #是否使用`htaccess`文件来管理该目录
    Order Deny,Allow   #访问优先级，越后面优先级越高
    Deny from 192.168.0.104 #拒绝该IP的访问
    Require all granted
</Directory>
```
`Options`常用设置：
 ![avatar](/中间件/Apache/Diretory路径配置.png) 

`AllowOverride` 常用设置：
![avatar](/中间件/Apache/AllowOverride.png) 


4. `<Location [url|path]>....</Location>` 用来对网络路径进行限制

5. `alias URI Directory` 目录映射,不同的URI映射到不同的目录站点。

PhP:

Mysql:

`my.cnf` 主要配置文件。

