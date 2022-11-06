### docker容器的使用
# 常规指令
1. 容器运行：`docker run (镜像) (应用程序)`  *<font size=2>如果镜像本地不存在，则从库里面拉取。类似于`docker pull (镜像)`</font>*
2. 与容器进行交互：`docker run -i -t (镜像) (应用程序)`
3. 容器后台运行：`docker run -d (镜像) (应用程序)` *<font size=2>返回唯一内码，可以通过该内码，获取运行信息。使用`docker attach`或`docker exec -it [容器名称|容器ID]`进入容器。</font>*
4. 查看正在运行的容器状态:`docker ps` 
5. 查看容器的标准输出流：`docker logs [容器名称|容器ID]`
6. 停止容器的运行：`docker stop [容器名称|容器ID]`
7. 启动容器的运行：`docker start [容器名称|容器ID]`
8. 查看所有容器的运行状态：`docker ps -a`  *<font size=2>通过该指令可以找到已经停止的容器名称和容器ID</font>*
9. 进入容器:`sudo docker exec -it [容器名称|容器ID] /bin/bash` *<font size=2>退出后容器依然运行</font>*
10. 进入容器：`sudo docker attach [容器名称|容器ID]` *<font size=2>退出后容器会关闭</font>*
11. 导出容器：`sudo docker export [容器名称|容器ID]  > ubuntu.tar`
12. 删除容器：`sudo docker rm -f [容器名称|容器ID]`
13. 查看容器运行标准输出：`sudo docker logs -f [容器名称|容器ID]` *<font size=2>查看方式类似于`tail -f`</font>*
14. 查看容器与本机的绑定端口：`sudo docker ports`

# 运行web
1. 下载镜像：`sudo docker pull 镜像`
2. 运行镜像：`sudo docker run -d -p (镜像) (应用程序)` *<font size=2>-p用来绑定到本机网络端口，没有设置则由容器自己选择</font>*