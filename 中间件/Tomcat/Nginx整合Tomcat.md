### Nginx整合Tomcat

# 代理与动静分离
核心指令为`proxy_pass`，用来创建对后台服务的代理，位于`location`模块中。
其他指令：
    - `proxy_buffering on|off;` 开放缓存功能，减少即时带宽。
    - `proxy_buffer_size 数量;` 设置缓存区的大小 
    - `proxy_buffer 数量` 设置缓存区的大小
    *<font size=2>``proxy_buffering`打开时proxy_buffer指令才有效</font>*
示例：
    ```
    server {
        listen       90;
        server_name  localhost;
        root   /usr/local/nginx/www;
        index index.html index.htm;
        location ~ \.jsp {
                #index index.jsp
                proxy_pass http://192.168.0.203:80;
        }

        location ~ \.(html|png|jpg|js|css|gif|bmp|swf|ico|svg)$ {
                expires 1d;
                root /usr/local/tomcat/webapps/ROOT;
        }
    }
    ```

# 负载均衡
主要指令：`upstream`,通过该指令设置对应的负载.
其他指令：`weight`,设置每个代理服务的域名的权重

    - 设置负载均衡模块
    ```
        upstream tomcatserver {
            server 127.0.0.1:8080;
            server 127.0.0.1:8081;
            server 127.0.0.1:8082;
        }
    ```
    - 调用对应的模块
    ```
        server {
                listen       90;
                server_name  localhost;
                root   /usr/local/nginx/www;
                index index.html index.htm;
                location ~ \.jsp {
                        #index index.jsp
                        proxy_pass http://tomcatserver;
                }
                location ~ \.(html|png|jpg|js|css|gif|bmp|swf|ico|svg)$ {
                        expires 1d;
                        root /usr/local/tomcat/webapps/ROOT;
                }
        }
    ```
