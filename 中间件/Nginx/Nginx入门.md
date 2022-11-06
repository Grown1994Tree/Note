# Nginx服务器入门

### 一、什么是Nginx?
Nginx是一种介于操作系统和应用程序的平台。跟Apache不同，Nginx是异步调用，具有备高性能、高扩展性、高可靠性、低内存消耗等优势。

### 二、Nginx安装(Ubuntu)
安装Nginx服务器需要先在本地安装`PCRE库`、`zlib库`以及`ssl`
由于`PCRE库`和`zlib库`都需要在本地编译，因此需要先安装编译环境
1. 安装编译环境：
    - Ubuntu:
    ```
        sudo apt-get install build-essential
        sudo apt-get install libtool
    ```
    - centOs
    ```
        sudo yum -y install gcc automake autoconf libtool make
        sudo yum install gcc gcc-c++
    ```
2. 安装`PCRE库`、`zlib库`以及`ssl`
    - 源码目录为:`/usr/local/src`
    - PCRE库：
        - 下载网址：`https://sourceforge.net/projects/pcre/files/pcre/` *<font size=2>软件包：pcre8-45.tar.gz</font>*
        - 解压后执行命令行进行安装
        ```
            cd pcre-8.45  <font size=2>解压后的pcre目录</font>
            ./configure
            make
            make install
        ```
    - zlib库
        - 下载网址：`http://zlib.net/`  *<font size=2>软件包：zlib-1.2.11.tar.gz</font>*
        - 解压后执行命令行进行安装
        ```
            cd zlib-1.2.11  <font size=2>解压后的zlib目录</font>
            ./configure
            make
            make install
        ```
    
    - ssl
        - 下载网址：`https://www.openssl.org/source/` *<font size=2>软件包： openssl-1.1.1l.tar.gz </font>*
        - 解压后执行命令行进行安装
        ```
            cd openssl-1.1.1l
            sudo ./config
            sudo ./Configture

        ```
3. 安装Nginx软件
    - Nginx
        - 下载网址：`https://nginx.org/en/download.html` *<font size=2>软件包： nginx-1.20.1.tar.gz </font>*
        - 解压后执行命令行进行安装
        ```
            cd nginx-1.20.1

            ./configure --sbin-path=/usr/local/nginx/nginx 
            --conf-path=/usr/local/nginx/nginx.conf \  
            --pid-path=/usr/local/nginx/nginx.pid \
            --with-http_ssl_module \  
            --with-pcre=/usr/local/src/pcre-8.34 \ 
            --with-zlib=/usr/local/src/zlib-1.2.8 \
            --with-openssl=/usr/local/src/openssl-1.0.1c 
            --n gx_http_core_module  
            make
            make install
        ```
        - 安装完成后运行`/usr/local/nginx/nginx`,在web端访问。
        ![avatar](/中间件/Nginx/安装成功.png)

        - 关闭服务`nginx -s quit`和`nginx -s stop`，`quit` 指令会等已经连接的请求完成后才关闭   
        - 加载服务`nginx -s reload` 重新加载配置文件

4. 配置自定义服务
通过配置自定义服务，我们可以使用`systemctl`指令对服务进行管理.
    - 在`/etc/systemd/system/`目录下建立`nginx.service`，内容如下： 
        ```
        [Unit]
        Description=A high performance web server and a reverse proxy server
        After=network.target

        [Service]
        Type=forking
        PIDFile=/usr/local/nginx/nginx.pid  #进程号
        ExecStartPre=/usr/local/nginx/nginx -t -q -g 'daemon on; master_process on;' 
        ExecStart=/usr/local/nginx/nginx -g 'daemon on; master_process on;' 
        ExecReload=/usr/local/nginx/nginx -g 'daemon on; master_process on;' -s reload
        ExecStop=/usr/local/nginx/nginx -s stop 
        TimeoutStopSec=5
        KillMode=mixed

        [Install]
        WantedBy=multi-user.target
        ```
    - 使用`ln` 指令将该文件软链接到 `/usr/lib/systemd/nginx`
这样就可以使用`systemctl`指令和`service`指令进行运行


### 三、基本配置（可以正常运行）
1. 配置文件主要分为两部分：`nginx.conf`主配置文件和站点配置文件
2. 站点配置文件在`sites-available`目录底下建立，软链接到`sites-enable`目录，这样可以根据情况选择需要打开的站点。*<font size=2>需要运行就软链接到`sites-enable`目录</font>*
3. 在`nginx.conf`主配置文件引入站点配置模块。
4. 配置文件解析：
    - 主要配置文件
    ```
        worker_processes  1;
        events {
            worker_connections  1024;
        }
        http {
            include       mime.types;
            default_type  application/octet-stream;
            sendfile        on;
            keepalive_timeout  65;
            include /usr/local/nginx/conf/*;   #引入配置文件
            include /usr/local/nginx/sites-enable/*; #引入战点配置文件
        }

    ```
    - 站点配置文件
    ```
        server {
            listen       80; #端口
            server_name  localhost;   #域名
            root   /usr/local/nginx/www;  #站点路径
            index index.html index.htm; #首页
            location / {  #路由
                try_files $uri $uri/ =404;
                }
        } 
    ```

### 四、CentOS上进行安装
1. 在环境中安装`pcre`、`zlib`和`openssl`模块
    - 确认是否已经安装好该模块 `rpm -qa zlib zlib-devel pcre pcre-devel openssl openssl-devel`
    - 跟Ubuntu不同，CentOs中可以直接使用`yum install zlib zlib-devel pcre pcre-devel openssl openssl-devel -y` 进行安装 

2. 下载nginx
    - 由于是在虚拟机中安装，所以使用`wget`指令下载nginx,url为下图。*<font size=2>如果无法使用`wget`指令，则使用`yum -y install wget`进行安装</font>*
     ![avatar](/中间件/Nginx/nginx.png)

3. 安装nginx
    ```
        ./configure\ 
        --prefix=/usr/nginx\ 
        --with-http_ssl_module\ 
        --with-http_stub_status_module

        make
        make install
    ```
通过以上指令可以配置nginx模块，使用`nginx -v`指令可以查看已经安装的模块。
*<font size=2>模块重新配置好后，只需运行到`make`，如果更改路径`--prefix`,则需要运行到`makd install`</font>*
