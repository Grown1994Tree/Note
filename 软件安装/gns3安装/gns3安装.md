# gns3安装

### 一、安装add-apt-repository脚本
add-apt-repository脚本由python-software-properties工具包提供
    - ubuntu 12.10之前的版本：`sudo apt-get install python-software-properties` 
    - ubuntu 12.10之后的版本:`sudo apt-get install software-properties-common` 
    - 使用python3环境：`sudo apt-get install python3-software-properties`

### 二、安装GNS3
1. 添加GNS3存储库：`sudo add-apt-repository ppa:gns3/ppa` *<font size=2>`add-apt-repository`工具用来添加个人软件包存档</font>*
![avatar](/软件安装/gns3安装/添加个人仓库.png)
*<font size=2>点击`ENTER`进行安装</font>*
2. 查看可以更新的软件:`sudo apt update` *<font size=2>只展示可以更新的数量，使用`apt list --upgradable`查看可以更新的软件内容</font>*                                
3. 安装gns3客户端和服务端：`sudo apt install gns3-gui gns3-server`

