# Maven

### 一、什么是Maven
1. 定义：一种项目构建工具和包管理工具。
主要功能：
    - 提供了一套标准化的项目结构；
    - 提供了一套标准化的构建流程（编译，测试，打包，发布……）；
    - 提供了一套依赖管理机制。

Maven项目目录结构：
a-maven-project
├── pom.xml
├── src
│   ├── main
│   │   ├── java
│   │   └── resources
│   └── test
│       ├── java
│       └── resources
└── target

*<font size=2>pom.xml是项目描述文件</font>*

2. 项目描述文件pom.xml
![avatar](/JAVA/Maven_项目文件描述.png)

- groupId 报名
- artifacId 类名
-  version 版本号
-  dependencies 依赖集合节点
-  dependency 单个依赖

<!--  Maven依赖关系 ，后面补充-->

### 二、构建流程
1. Maven用来实现自动化编译，打包，测试，发布步陬。
2. 流程
   - 
   

主要使用两个流程，`default`和`clean`

### 三、
