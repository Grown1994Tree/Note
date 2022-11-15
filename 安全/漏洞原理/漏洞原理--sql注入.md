### 一、漏洞原理
利用现有程序(如表单、url请求等)把payload作为参数传递，使原有的SQL语句产生歧义，从而实现攻击效果。
### 二、存在条件

- 程序的调用过程中涉及到数据库的使用
- 程序没有对参数进行筛选和判定
### 三、SQL注入分类
![](https://cdn.nlark.com/yuque/0/2022/jpeg/32589116/1661656998777-77067759-6c2a-427f-b7de-45f3ed3e0ee0.jpeg)
> 把SQL语句的执行结果会展示到界面上，为显注；不展示到页面上则为盲注

### 四、注入过程

1. 显注
   1. 判定注入类型：输入1',如果页面展示出错误信息，则为显注漏洞，我们可以推测原来的sql语句为'$id'
   2. 判定显示字段：通过输入1' order by 1,2,3.....# ，我们可以根据其报错的位置来判定该SQL语句展示几个字段![image-20220218140529221.png](https://cdn.nlark.com/yuque/0/2022/png/32589116/1661669738776-426149d6-e048-4875-830c-57e86fa47204.png#clientId=u1fd48911-6855-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=133&id=uc9e62c0c&margin=%5Bobject%20Object%5D&name=image-20220218140529221.png&originHeight=166&originWidth=1200&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36279&status=done&style=none&taskId=u5bab7575-17ef-4a82-99de-09ebc5c38a9&title=&width=960)
   3. 判定展示字段：通过输入1' and 1=2 union select 1,2,3%23，判断有哪几个字段展示出来确认展示位
   4. 取数：通过b、c，我们可以利用mysql的元数据库对敏感数据依次进行获取。通常按照数据库、表以及字段等数据获取敏感数据
2. 布尔盲注
   1. 判断注入类型：依次输入以下payload，1'#、1' and 1=1# 以及1' and 1=2# ，如果出现前两种一致且都跟第三种不一致的情况，我们可以认定存在布尔盲注的情况
   2. 取数：跟显注不同，盲注无法直接把结果展示出来，因此根据展示的结果不一致来猜数，通常配合burpsuite工具使用。
      1. 猜数量：输入payload 1' and (select count(schema_name) from information_schema.schemata)=8%23,我们可以确认库的数量
      2. 猜长度：输入payload 1' and length(user())=14%23，如果展示结果跟1'一致，则说明长度是正确的，也就是说我们获取了表的长度。
      3. 猜字符：输入payload 1' and substr(user(),1,1)='d'%23，如果展示结果跟1'一致，则说明对应字符是正确的，我们可以依次获取每个字符，从而获取表名
      4. 通过上面三个步骤，我们可以利用mysql的元数据库对敏感数据依次进行获取。通常按照数据库、表以及字段等数据获取敏感数据
3. 时间盲注
   1. 判断注入漏洞：输入payload,1' and if(5>1,sleep(5),1)%23,因为页面无法提供其他信息，通过sleep的暂停时间来判断是否可以进行注入
   2. 取数：跟布尔盲注一样的流程，只是改用sleep函数进行判断
### 五、常用注入方式

1. XPATH报错注入
   1. 条件：利用mysql新两个xml相关的函数extractvalue和updatexml
> 1" union select extractvalue(1,concat('!',(select database())));%23
>         1" union select updatexml(1,concat('!',(select database())),1);%23

