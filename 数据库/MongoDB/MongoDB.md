# MongoDB数据库

### 什么是MongoDB数据库。
1. MongoDB数据库是一种非关系型数据库，采用类似于`json`的格式来对数据进行处理，避免了关系型数据库导致的数据之间关联造成的性能瓶颈。
2. 跟关系型数据库相比，在存储类型以及表之间的关联更加灵活
3. 采用集合的方式进行存储，集合类似于表，文档类似于表中的每一行,一个库里面拥有多个集合
4. 文档关联结构（两种方式）：
    - 嵌入式关系：文档以数组的形式嵌入另一个文档
    ```
        {
            "name": "Tom Hanks",
            "contact": "987654321",
            "dob": "01-01-1991",
            "address":
            [{
                "building": "22 A, Indiana Apt",
                "pincode": 123456,
                "city": "chengdu",
                "state": "sichuan"
            },
            {
                "building": "170 A, Acropolis Apt",
                "pincode": 456789,
                "city": "beijing",
                "state": "beijing"
            }]
        }
    ```
    - 引用式关系：在一个文档内嵌入另一个文档的ID
    ```
        {
            "name": "Tom Benzamin",
            "contact": "987654321",
            "dob": "01-01-1991",
            "address_ids": [
                ObjectId("52ffc4a5d85242602e000000")    #对应address文档的id字段
            ]
        }
    ```
5. 元数据（需要补充）


### 安装
安装指令：`sudo apt-get install mongodb`

### 常用命令
1. 查看和切换数据库
    - `show dbs` 展示所有数据库 *<font size=2>类似：show databases</font>* 
    - `db` 显示当前连接的数据库 *<font size=2>类似：select database()</font>* 
    - `use [数据库名]` 切换和创建数据库，如果没有数据库，则创建一个数据库  *<font size=2>切换跟mysql一致，创建mysql为create database 数据库名</font>*

2. 销毁数据库
    - `db.dropDatabase()` 销毁数据库，`db`指向当前数据库,因此删除前需要使用`use [数据库名]`进行切换   *<font size=2>类似：drop database zabbix</font>* 
![avatar](/数据库/MongoDB/销毁数据库.png)

3. 创建和销毁集合
    - `db.createCollection(集合名)` 创建集合，集合名要加引号 <font size=2>由于Mysql需要设置类型结构，因此相比于mongo会更加复杂</font>* 
    - `show collections` 展示数据库对应的集合
    - `db.数据库名.drop()` 删除对应数据库名
    ![avatar](/数据库/MongoDB/销毁集合.png)

4. 插入文档
 - 使用`db.数据库名.insert()` 或 `db.数据库名.save()` 两者都会插入文档，insert只能插入新的文档，save除了插入新的文档外还能保存文档。 *<font size=2>是否相同通过主键来比较，主键怎么设置呢</font>*
  ![avatar](/数据库/MongoDB/插入文档.png)

5. 查询数据
 - `db.集合名.find()` 查找集合里面的所有文档
 - `db.集合名.find({ key1: value1, key2: value2 }).pretty()` 类似于关系型数据库中的`and`
 - `db.集合名.find({$or:[{key1: value1},{key2: value2}]}).pretty()` 类似于关系型数据库中的`or`
 - 后缀方法：
    - `pretty()` 格式化dson格式，更好的展示
    - `limit(数值)`  限制展示数量，默认从第一行开始
    - `skip(数值)`   展示时跳过前几行
    - `sort(对象)`   对象里面key为要排序的内容，value为方向。1为升序，-1为降序
    - `explain()`  查询分析，通过该函数可以查看查询中使用查询索引的效率，以便于优化
    - `hint(索引对象)` 硬性要求使用索引进行查询
比较和筛选：key代表着要查询的字段，value代表要查询字段的范围。
可以通过正则表达式或者比较符来筛选

6. 创建索引：
    - `db.集合名.ensureIndex(索引内容，可选参数)` 建立索引
        - 索引内容：键值对，由建立索引的字段组成。`{keyName:1|-1}`keyName为字段名，1|-1为排序。
         ![avatar](/数据库/MongoDB/索引.png)

7. 原子操作:
    - `db.集合名.findAndModify(原子对象)`  对象里面包含查询和更新两个方法来保证更新的原子性，但只能对单个文档。
    


### 条件操作符
主要格式为`{key:{比较|类型：条件}}`
- 比较：
```
    $gt：大于
    $lt：小于
    $gte：大于等于
    $lte：小于等于

```
- 类型（$type）：
```

    1: 双精度型(Double)
    2: 字符串(String)
    3: 对象(Object)
    4: 数组(Array)
    5: 二进制数据(Binary data)
    7: 对象 ID(Object id)
    8: 布尔类型(Boolean)
    9: 日期(Date)
    10: 空(Null)
    11: 正则表达式(Regular Expression)
    13: JS 代码(Javascript)
    14: 符号(Symbol)
    15: 有作用域的 JS 代码(JavaScript with scope)
    16: 32 位整型数(32-bit integer)
    17: 时间戳(Timestamp)
    18: 64 位整型数(64-bit integer)
    -1: 最小值(Min key)
    127: 最大值(Max key)

```