# 找回Mysql密码

### 一、免密登陆
1. 使用`systemctl stop mysql`关闭mysql服务。
2. 找到`mysqld`指令，使用`mysqld --skip-grant-tables` 服务重新启动mysql服务。
3. 直接使用`mysql -u root`进行免密登陆。
4. 重新修改root密码后，再使用`flush privileges;`更新内存。
5. 关闭掉使用`mysqld --skip-grant-tables`运行的窗口。

### 二、更新密码
1. 使用update语句进行更新
`update mysql.user set authentication_string=password('密码') where user='root'`
*<font size=2>在5.7以后的版本库中，更改密码时使用`authentication_string`代替`password`</font>*