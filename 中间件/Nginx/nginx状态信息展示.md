1. 要先安装`-with-http_stub_status_module`模块
2. 新建虚拟主机:
```
    server{
        listen 9001;
        server_name status.sjtest.com;
        location /status {
            stub_status on;  状态信息为开
            access_log off;
        }	
    }
```

3. 访问：`http://192.168.0.103:9001/status`