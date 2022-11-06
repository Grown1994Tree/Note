# 什么是docker?

### 一、docker平台的特点
1. 区分基础架构和应用程序
2. 实现应用程序的开发、交付和运行
3. 一次开发，多地部署。
4. 轻巧，可移植相对于虚拟机可以节省更多的资源。

### 二、概念
1. dockerfile:类似于源代码
2. image：镜像，类似于可执行文件或者类。
3. container: 容器，类似于进程或者对象。
4. Repository： 仓库，用来存储镜像

### 三、安装
Ubuntu
1. 删除旧版本：`sudo apt-get remove docker docker-engine docker.io containerd runc` *<font size=2>新版本和旧版本所依赖的安装包不一致，需要重新调整</font>*

*<font size=2>2-6用来安装docker</font>*
2. 更新包索引：`sudo apt-get update`
3. 安装https传输依赖 `sudo apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common`
4. 添加GPG密钥：`curl -fsSL https://mirrors.ustc.edu.cn/docker-ce/linux/debian/gpg | sudo apt-key add -`
5. 验证是否带有指纹的密钥：`sudo apt-key fingerprint 0EBFCD88` *<font size=2>完整指纹：9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88 </font>*
6. 完成仓库的安装：`sudo add-apt-repository "deb [arch=amd64] https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu/ $(lsb_release -cs) stable"`

*<font size=2>7、8选择任意一条进行安装</font>*
7. 安装docker最新版:`sudo apt-get install docker-ce docker-ce-cli containerd.io`
8. 安装docker指定版本
    - 查看现有可用版本：`apt-cache madison docker-ce` *<font size=2>从这里找到想要安装的版本</font>*
    - 对选择版本进行安装：`sudo apt-get install docker-ce=<VERSION_STRING> docker-ce-cli=<VERSION_STRING> containerd.io`

9. 验证是否安装成功：`sudo docker run hello-world`


