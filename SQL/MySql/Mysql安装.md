# mysql安装

### 一、安装内容
1. 命令行:
    - `sudo apt-get install mysql-server`
    - `sudo apt-get install mysql-client`
    *<font size=2>服务端和客户端都要安装</font>*
2. 配置目录：
    - 在linux中，mysql的配置文件都放置在`/etc/mysql`目录中。

### 二、sql基本语法。
1. 常用的数据类型
    - `char` 和 `varchar` 的区别：两者根据数值确定最大值，但是在范围内`varchar`会根据实际空间缩小
    - `ENUM` 和 `SET` : `ENUM` 为单选，`SET` 为多选,只能插入设置的选项
    ![avatar](/SQL/MySql/数据类型.png)   

2. 导入数据
    指令：`source [数据包]`  
    - 该指令要在mysql控制台执行，可以通过`>`重定向数据到其他文件
    - 数据包要满足格式utf8,可以使用`set names [字符格式]`指令进行改变。

3. 约束内容
    - 主键约束：
        - 方法一：在字段列名后面添加`primary key` *<font size=2>只能处理单主键，如果遇到复合主键将只能使用方法二</font>*
        - 方法二：在字段列表后面添加`constraint [主键名] primary key(主键，主键.....)`  *<font size=2>可以设置单主键和复合主键</font>*
    - 默认约束：`default [默认值]` 主要在插入语句没有插入该字段的值，用来设置为默认值。
    - 唯一值约束：使用`unique(字段，字段....)`，如果使用插入语句时，遇到重复则会跳出错误框
    - 外健约束：
        - 方式一：在创建语句的尾部添加` CONSTRAINT [外键名] FOREIGN KEY (外键字段) REFERENCES department([约束表字段名])` 在插入或者删除时，保证两张关联表一致。
        - 方式二：对应字段后面加上`REFERENCES department([约束表字段名]` 语句
    - 非空约束： 在字段后面设置 `not null` 来避免出现`null`值
    ![avatar](/SQL/MySql/约束内容.png) 

4. 通配符
    - 配合like语句使用
    - `_`匹配单个字符，`%`匹配多个字符




### 错误整理
1. 在创造数据库时，避免把`()`写成`{}`
 ![avatar](/SQL/MySql/错误记录-大括号和小括号.png) 

2. 使用内置函数的注意事项，如果查询语句使用内置函数时，就无法跟单个字段一起出来
 ![avatar](/SQL/MySql/错误记录-内置函数.png) 
 ![avatar](/SQL/MySql/内置函数.png) 