### Tomcat

### Tomcat下载
下载地址：https://tomcat.apache.org/ 
![avatar](/中间件/Tomcat/下载地址.png)

### 配置环境
系统变量配置：
在Ubuntu中，主要是在`/etc/profile`和`/etc/profile.d`里面配置。`/etc/profile`文件会读取`/etc/profile.d`目录底下的配置文件并依次执行。
```
        if [ -d /etc/profile.d ]; then
        for i in /etc/profile.d/*.sh; do
            if [ -r $i ]; then
            . $i
            fi
        done
        unset i
        fi
```
因此，需要在`/etc/profile.d`创建对应的配置文件即可

1. 配置JAVA运行环境
    - 在`/etc/profile.d`目录里面`jre.sh`文件
    ```
        export JRE_HOME=/usr/local/jre
        export PATH=$JRE_HOME/bin:$PATH
    ```
    - 使用`java -version`验证
    ![avatar](/中间件/Tomcat/java环境配置.png)

2. 配置Tomcat运行环境
    - 在`/etc/profile.d`目录里面`tomcat.sh`文件
    ```
        export CATALINA_HOME=/usr/local/tomcat
        export PATH=$CATALINA_HOME/bin:$PATH
    ```
    - 在`setclasspath.sh`文件夹里面设置JRE_HOME路径后启动即可以正常访问。
    ![avatar](/中间件/Tomcat/启动测试.png)

3. 设置多个Tomcat实例
    - `CATALINA_HOME`和`CATALINA_BASE`的差异。
        - `CATALINA_HOME`：配置安装路径
        - `CATALINA_BASE`：配置运行时路径 *<font size=2>设置单实例时,`CATALINA_BASE`路径默认为`CATALINA_HOME`的路径</font>*
    
    - 创建多个实例目录，并移动对应的目录，可以使用shell语句进行批量处理
    ```
        #!/bin/bash
        #方案为先生成一个目录，然后使用该目录进行复制
        #创建目标目录函数，goal.conf为需要创建的目录
        function makeGoalDir(){
                for i in $(cat goal.conf)
            do
                echo $i
                cp -rf $1 $i
            done
            rm -rf $1  #删除备份目录
        }

        SOURCEPATH=$(cat source.conf)
        BAKPATH=/usr/local/tomcat_base_bak
        mkdir $BAKPATH
        #生成备份目录，并从安装目录复制需要的文件夹到备份目录
        for i in $(cat file.conf)
        do
            file=$SOURCEPATH/$i
            cp -rf $file $BAKPATH
        done

        makeGoalDir $BAKPATH 
    ```
    - 创建`startup.sh`文件和修改文件`conf/server.xml`的端口
    ```
        #!/bin/sh
        #设置对应的环境
        export CATALINA_HOME=/usr/local/tomcat
        export CATALINA_BASE=/usr/local/tomcat_base_1
        cd $CATALINA_HOME
        ./bin/catalina.sh start
    ```
