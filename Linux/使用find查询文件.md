#使用find查询文件

一、基本语法
`find [查询目录] [查询深度参数] [索引内容参数] [查询内容]`

士例：
`find ./ -maxdepth 2 -name '*.txt'`

1. ./   _为目录_
2. -maxdepth 2   _为查询深度，1为只查询本层。_
3. -name   _根据类型进行查询，name为根据文件名来查询_
常用参数:
    **-name	按名称查找S**
    **-size	按大小查找**
    **-user	按属性查找**
    **-type	按类型查找**
    **-iname 忽略大小写**
4. "*.txt"  _查询以txt为后缀的文件_

二、合并查询
实例：
`find ./ -maxdepth 1 \( -name '*.txt' -o -name '*.pdf' \)`

**括号`()`需要在前面加转义字符\\**

三、配合管道和grep进行使用。
实例：
`find -name '*.txt' | grep ./a.txt > list1.txt`

通过`find -name '*.txt' `找出对应的文件目录路径，并写入管道
`grep ./a.txt > list1.txt` 对写入的内容进行筛选并提取到list1.txt里面。




