# Redis数据库

### 安装和使用
1. 安装指令：`sudo apt-get install redis`
2. 启动：`sudo systemctl start redis` *<font size=2>如果无法启动，可以直接使用路径启动：`/usr/bin/redis-server`，同时启动后的命令框不能关闭</font>*
![avatar](/数据库/Redis/安装.png)
3. 进入数据库：`redis-cli`
4. 采用C/S模式，先启动服务端，再启动客户端

### 常用指令
1. 字符串（最大容纳512M）：
    - 设置字符串值：`set key value [option]`
        - `nx`: 使用该选项时，`key`一定不能存在过
        - `xx`: 使用该选项时，`key`一定要存在
    - 获取字符串值：`get [key]`
    升级版
    - 同时设置多个字符串值:`mset key value`
    - 同时获取多个字符串值:`mget key`


2. 列表（容量较大）
    - 从左边添加值进入类表：`lpush key value [value] [value]` 
    - 从右边添加值进入类表：`rpush key value [value] [value]`
    - 展示列表里面的值：`lrange key firstIndex lastIndex`
    - 从列表左侧擅除：`lpop key value`
    - 从列表右侧擅除：`rpop key value`

3. HASH（用来存储对象）
    - 设置多个键值对：`hmset obj key1 value1 [key2] [value2]....`
    - 获取多个值：`hmget obj key1 [key2]....`
    - 设置单个键值对：`hset obj key1 value1`
    - 获取单个值：`hget obj key1`
    - 获取对象所有值: `hgetall obj`
    - 对对象的整数值进行修改：`hincrby obj key value` *<font size=2>如果对应key存在就添加，否则在该hash表新建一个键值对。只能在整数型使用</font>*
    ![avatar](/数据库/Redis/heset1.png)
    ![avatar](/数据库/Redis/hincrby.png)

4. 无序集合(类似无序列表，会去除调重复值)
    - 加入集合:`sadd 集合名 value1 value2 value3`
    - 展示集合：`smembers 集合名`
    - 判断集合或者集合的值是否存在：`sismember 集合名 [value]`
    ![avatar](/数据库/Redis/set.png)

5. 有序集合(类似有序列表，会去除调重复值，相比于无序列表，增加了权值来进行排列)
    - 加入集合:`zadd 集合名 权值 value [权值] [value]`
    - 展示集合:`zrange|zrevrange 集合名`
    ![avatar](/数据库/Redis/zadd.png)

6. 通用指令
    - `exist key`: 判断key是否存在
    - `del key`: 删除某key
    - `type key`: 判断key所属的值的类型
    - `keys 模板`: 列出匹配的key
    - `randomkey`: 获取随机key
    - `rename oldname newname`：更改 key 的名字，新key如果存在将被覆盖
    - `rename oldname newname` : 更改 key 的名字，新key如果存在将会报错
    - `dbsize`: 获取key数
    - `flushdb`: 清除当前数据库的所有key
    - `flushall`: 清除所有数据库的所有key

7. 时间指令
    - `expire key 秒数`：设定该key什么时候被情空。 *<font size=2>可以以`ex 秒数`的形式设置在set指令后面</font>*
    - `ttl key` : 查看当前指令还剩余多久被清空

8. 配置信息获取
    - `config set key value` 设置配置信息
    - `config get key` 获取配置信息 

### 高级应用
1. 安全性：在redis中，每秒可以设置150K次的密码尝试，因此需要设置强有力的密码
    - `config set requirepass [password]` 该指令用来进行密码设置
    - `redis-cli -a [password]` 使用该指令在登陆时进行验证
    - `auth [password]` 如果已经等了，则使用该指令进行验证
    *<font size=2>需要使用密码登陆后才能查看key的值</font>*

2. 主从复制，一个主服务器master可以配置多个从服务器slave （后续补充操作）
    - 目的：
        - 功能拆分，有些服务器用来读，有些用来写入等
        - 互为备份，当某些服务崩溃后，slave可以转为master来使用

3. 事务：用来进行执行语句的批量执行。*<font size=2>无法保持一致性</font>*
    - 指令:`multi`和`exec`
     ![avatar](/数据库/Redis/事务.png)

4. 持久化机制：用来保证内存中的数据在系统重启后不丢失
两种方案：
    - `save [时间] [keys]` 在给定的时间范围内，超过keys时就保存一个快照
    - `Append-only file`（缩写为 aof） 保存读写操作到磁盘里面。