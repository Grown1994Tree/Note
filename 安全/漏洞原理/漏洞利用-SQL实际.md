### 一、注入类型判定
1. web后台常用格式
```sql
$sql = "SELECT * FROM users WHERE id = $id LIMIT 0,1";
$sql = "SELECT * FROM users WHERE id = '$id' LIMIT 0,1";
$sql = 'SELECT * FROM users WHERE id = "$id" LIMIT 0,1';
$sql = "SELECT * FROM users WHERE id = ('$id') LIMIT 0,1";
$sql = 'SELECT * FROM users WHERE id = ("$id") LIMIT 0,1';
$sql = "SELECT * FROM users WHERE id = (('$id')) LIMIT 0,1";
$sql = 'SELECT * FROM users WHERE id = (("$id")) LIMIT 0,1';
```
因此，可以通过输入以下payload进行闭合
> 1#
> 1'# 
> 1"#
> 1')# 
> ')) #
> ') # 
> ")) #

### 二、攻击方式


### 三、攻击绕过


