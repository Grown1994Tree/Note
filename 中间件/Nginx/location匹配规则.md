# 一、location分解

1. 基本配置：`location [参数] [路径] [指令块]`
```
location = /admin/ {
    # The configuration you place here only applies to
    # http://website.com/admin/
}
```
2. 匹配优先级
```
    精确匹配 =
    前缀匹配 ^~（立刻停止后续的正则搜索）
    按文件中顺序的正则匹配 ~或~*
    匹配不带任何修饰的前缀匹配
```
*<font size=2>对于普通匹配来说，优先匹配路径较长的；对于正则匹配来说，按照顺序</font>*

3. 常规指令
```
    location ~ /test/ {
	    root  html;
	   # index  index.html;
	    try_files $uri $uri/ /index.html;
	}
```
- 当访问`http://192.168.0.103:9000/test/`时，先会找到`html/test/`目录，然后根据`index`和`try_files`指令找到对应的文件
- `index`指令：强制路径，必须访问`index`设置的路径，否则报错
- `try_files $uri`指令:会先匹配路径提供的文件名，如果没有再使用默认文件

