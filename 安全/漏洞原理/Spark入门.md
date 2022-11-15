### 一、Spark安装
1. 上传软件到指定目录，并设置启动环境
```shell
# java 环境
export JAVA_HOME=/usr/java
export PATH=$PATH:$JAVA_HOME/bin

#SPARK_HOME
export SPARK_HOME=/opt/spark-3.3.0-bin-hadoop3/
export PATH=$PATH:$SPARK_HOME/bin
```
验证：出现路径，说明环境配置成功
>  which spark-shell
> /opt/spark-3.3.0-bin-hadoop3/bin/spark-shell


2. 修改配置文件
- 配置环境变量
```shell
export JAVA_HOME=/usr/java
export SCALA_HOME=/usr/share/scala
export SPARK_HOME=/opt/spark-3.3.0-bin-hadoop3/
export SPARK_MASTER_HOST=hadoop101
```

- 配置日志展示
```shell
# rootLogger.level = info
rootLogger.level = WARN
```
> 展示warn以上的信息， Log4j建议只使用四个级别，优先级从高到低分别是 ERROR、WARN、INFO、DEBUG 

- 增加从节点

![image.png](https://cdn.nlark.com/yuque/0/2022/png/32589116/1664202473603-1c0d7d46-6b88-4265-a53a-8b34f4f438ac.png#clientId=u78817db3-e223-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=345&id=ub7417596&margin=%5Bobject%20Object%5D&name=image.png&originHeight=431&originWidth=738&originalType=binary&ratio=1&rotation=0&showTitle=false&size=32941&status=done&style=none&taskId=u2e0263a7-3e19-431b-8c15-8ecb40f1e09&title=&width=590.4)
> 加入节点后，需要在`/etc/hosts`文件里面设置映射


3. 启动
- 启动服务：/opt/spark-3.3.0-bin-hadoop3/sbin/start-all.sh
> 同时启动主节点和从节点，访问[http://192.168.11.134:8080/](http://192.168.11.134:8080/)

![image.png](https://cdn.nlark.com/yuque/0/2022/png/32589116/1664202108158-60701257-9bef-4fd6-968b-5055026f7d1c.png#clientId=u78817db3-e223-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=650&id=u6d3a526d&margin=%5Bobject%20Object%5D&name=image.png&originHeight=813&originWidth=1909&originalType=binary&ratio=1&rotation=0&showTitle=false&size=96404&status=done&style=none&taskId=u8cc55785-5af0-482a-8534-5224394efe3&title=&width=1527.2)

- 启动交互界面
> MASTER=spark://hadoop101:7077 spark-shell  #MASTER需要大写

![image.png](https://cdn.nlark.com/yuque/0/2022/png/32589116/1664202286408-578a9ea8-f713-411b-af6c-439cc4f87b03.png#clientId=u78817db3-e223-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=265&id=u7193a7a3&margin=%5Bobject%20Object%5D&name=image.png&originHeight=331&originWidth=1449&originalType=binary&ratio=1&rotation=0&showTitle=false&size=25075&status=done&style=none&taskId=u0a1867d0-f8d5-4ec0-9ccf-28b996edd28&title=&width=1159.2)

- 关闭服务: /opt/spark-3.3.0-bin-hadoop3/sbin/stop-all.sh

### 二、RDD使用

1. RDD定义：Spark中数据的最基本抽象，有转换和行动两个方法
2. 操作流程
- 创建RDD
```scala
//从内存创建
val l1=sc.makeRDD(List(1,2,3,4,5))
l1.collect().mkString(",")
val l2=sc.parallelize(Array(6,7,8,9))
l2.collect().mkString(":")

//从外部文件创建
val f1=sc.textFile("/etc/passwd")
f1.collect()

```
