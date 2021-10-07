# JAVA概念解析

### 一、classpath 
1. 定义：JVM（JAVA虚拟机）的环境变量，用来帮助JVM查找和引人运行所需的`.class`文件
    -  JVM在运行时会先在当前目录查找`.class`文件，如果没有找到再去环境变量查找
    -  window配置路径:`C:\work\project1\bin;C:\shared;"D:\My Documents\project1\bin"`
    - Linux配置路径：`/usr/shared:/usr/local/bin:/home/liaoxuefeng/bin`
  
2. 配置`classpath`路径时，分为系统配置和运行时配置。在系统里面配置`classpath`时，会污染系统的环境，因此建议使用运行时配置。
   -  使用`java -classpath` 指令或`java -cp` 给虚拟机传递`classpath`
  
  3. JVM会自己本身就拥有核心库，因此就没有必要告知核心库的位置

### 二、jar包
1. 一种使用zip格式的压缩包，后缀由`.zip`改为`.jsr`
2. 用来管理打包和管理大量的类文件
   - 如果包内含有`/META-INF/MANIFEST.MF`文件且文件里面标明了`main-class`，则可以运行该包。
   -   在`/META-INF/MANIFEST.MF`可以配置`classpath`，用来包含和引人其他包。