# mysql安装

### 一、安装内容
1. 命令行:
    - `sudo apt-get install mysql-server`
    - `sudo apt-get install mysql-client`
    *<font size=2>服务端和客户端都要安装</font>*
2. 配置目录：
    - 在linux中，mysql的配置文件都放置在`/etc/mysql`目录中。
    - 主配置文件为`my.cnf`
### 二、sql基本语法。
1. 常用的数据类型
    - `char` 和 `varchar` 的区别：两者根据数值确定最大值，但是在范围内`varchar`会根据实际空间缩小
    - `ENUM` 和 `SET` : `ENUM` 为单选，`SET` 为多选,只能插入设置的选项
    ![avatar](/数据库/MySql/数据类型.png)   

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
    ![avatar](/数据库/MySql/约束内容.png) 

4. 通配符
    - 配合like语句使用
    - `_`匹配单个字符，`%`匹配多个字符

5. 更改数据表名的常用方法：
    `RENAME TABLE 原名 TO 新名字;`
    `ALTER TABLE 原名 RENAME 新名;`
    `ALTER TABLE 原名 RENAME TO 新名;`

6. 增加表列
    `ALTER TABLE 表名字 ADD COLUMN 列名字 数据类型 约束;` 
    `ALTER TABLE 表名字 ADD 列名字 数据类型 约束;`

7. 删除表列
    `ALTER TABLE 表名字 DROP COLUMN 列名字;`
    `ALTER TABLE 表名字 DROP 列名字;`

8. 重新设置字段类型
*<font size=2>可能会导致数据丢失</font>*
    `ALTER TABLE 表名字 CHANGE 原列名 新列名 数据类型 约束;`
    `ALTER TABLE 表名字 MODIFY 列名字 新数据类型;`

9. 添加索引 
    `ALTER TABLE 表名字 ADD INDEX 索引名 (列名);`
    `CREATE INDEX 索引名 ON 表名字 (列名);`

10. 创建视图语句
    `CREATE VIEW 视图名(列a,列b,列c) AS SELECT 列1,列2,列3 FROM 表名字;`

11. 导入纯数据
    `LOAD DATA INFILE '文件路径和文件名' INTO TABLE 表名字;` 

12. 导出数据
    `SELECT 列1，列2 INTO OUTFILE '文件路径和文件名' FROM 表名字;` *<font size=2>因为三导出到外部文件，所以需要`OUTFILE`关键字</font>*

    *<font size=2>对于11.12来说`文件路径和文件名`不是任意目录都可以，需要安全目录里面的文件夹才可以。通常使用`show variables like '%secure%'`指令查看安全目录</font>*

13. 创建数据库
    `create database JBBoss`

### 三、备份与还原
主要命令: `mysqldump`
`mysqldump -u root /数据库/名>备份文件名; `  #备份整个/数据库/
`mysqldump -u root /数据库/名 表名字>备份文件名;`  #备份整个表

还原方式：
1. mysql控制面版使用`source`指令
2. 命令行使用`<`指令

### 错误整理
1. 在创造/数据库/时，避免把`()`写成`{}`
 ![avatar](/数据库/MySql/错误记录-大括号和小括号.png) 

2. 使用内置函数的注意事项，如果查询语句使用内置函数时，就无法跟单个字段一起出来
 ![avatar](/数据库/MySql/错误记录-内置函数.png) 
 ![avatar](/数据库/MySql/内置函数.png) 

3. 插入用户报错
    - 操作：使用插入语句新建用户：`insert into user(Host,User,Password) values("localhost","pythonUser",password("123456"));`
    - 报错：`ERROR 1364 (HY000): Field 'ssl_cipher' doesn't have a default value`
    - 原因：Mysql的默认配置为严格模式，禁止使用`insert`语句插入用户。
    - 方案：
        - 调整`my.cnf`配置文件
        - 使用其他语句
        ```
        # 创建用户pythontest,密码为123456，主机为localhost 严格模式允许的语句
        create user 'pythontest'@'localhost' identified by '123456';
        # 给用户pythontest授予所有数据库的权限
        grant all privileges on *.* to 'pythontest'@'localhost' identified by '123456';

        ```
4. 插入值时，跳出`Field 'id' doesn't have a default value`错误
    - 原因：没有把主键设置为自增。
    - 方案：
        对于已经有的字段：`alter table content modify id int auto_increment;`
        新建表：对应字段添加`auto_increment`
