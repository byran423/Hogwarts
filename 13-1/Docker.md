## Docker 常用命令
#### 基本命令
docker version
docker info
#### 镜像管理
* 查看所有镜像：docker images
* 搜索镜像：docker search nginx
* 拉取下载：docker pull busybox:lastest
* 导出：docker save busybox 
* 导入：docker load < busybox.tar
* 删除：docker rmi busybox:lastest
* 更改镜像名：docker tag busybox:lastest busybox:test
* 查看镜像创建历史：docker history busybox
#### 容器管理
* 运行容器：docker run -d --name=busybox busybox:latest ping 114.114.114.114
* 查看运行的容器：docker ps、docker ps -a
* 查看容器中运行的进程：docker top busybox
* 查看资源占用：docker stats busybox
* 容器：docker start/restart/stop/kill busybox
* 暂停容器：docker pause/unpause busybox
* 强制删除容器：docker rm -f busybox
* 执行命令：docker exec -it busybox ls
* 复制文件：docker cp busybox:/etc/hosts .
* 查看容器日志：docker logs -f busybox
* 查看容器/镜像的元信息：docker inspect busybox
    * 格式化输出：docker inspect -f '{{.Id}}' busybox
    * Inspecty 语法可以网上查找
* 查看容器内文件结构：docker diff busybox

## 搭建Web服务器Nginx
#### Nginx 简介
* Nginx 是一个异步的Web服务器，主要提供Web服务、反向代理、负载均衡和Http缓存功能。创建与2004年，使用C语言开发
#### 运行Nginx容器
* 拉取：docker pull nginx:1.17.9
* 运行 docker run -d --name nginx -p 80:80 nginx:1.17.9
* 挂载目录：docker run -d --name nginx1 -p 8089:80 -v ${PWD}/nginx/html:/usr/share/nginx/html nginx:1.17.9

## 搭建测试用例管理平台Testlink
#### Testlink 简介
* Testlink 是基于WEB的测试用例管理系统，主要功能是：测试项目管理、产品需求管理、测试用例管理、测试计划管理、测试用例创建、管理和执行，并且还提供了统计功能
#### 部署数据库
* 创建容器网络 ：docker network create testlink
* 运行数据库：
* docker run -d --name mariadb -e ALLOW_EMPTY_PASSWORD=yes -e MARIADB_USER=bn_testlink -e MARIADB_DATABASE=bitnami_testlink --net testlink -v mariadb:/bitnami bitnami/mariadb:10.3.22
#### 部署Testlink
* 运行Testlink：
* docker run -d --name testlink -p 8001:8080 -p 8443:8443 -e ALLOW_EMPTY_PASSWORD=yes -e TESTLINK_DATABASE_USER=bn_testlink -e TESTLINK_DATABASE_NAME=bitnami_testlink --net testlink -v testlink:/bitnami bitnami/testlink:1.9.20
* 默认用户名：user，默认密码：bitnami
*访问地址：http://ip:8001
## 搭建持续集成平台
#### Jenkins简介
* Jenkins 是开源CI&CD软件领导着，提供持续集成和持续交付服务，有超过1000个插件来支持构建、部署、自动化，满足任何项目的需要
#### 部署Jenkins
* Docker hub: https://hub.docker.com/r/jenkins/jenkins/
* 运行：docker run -d --name=jenkins -p 8082:8080 jenkins/jenkins
* 查看默认密码：docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword
* 挂载目录：chmod 777 jenkins
  * 运行：docker run --name jenkins -d -p 8082:8080 -p 50000:50000 -v ${PWD}/jenkins:/var/jenkins_home jenkins/jenkins
#### Docker-compose 简介
* Docker-compose 是定义和运行多容器的Docker应用程序的工具。通过Compose，可以使用YAML文件来配置应用程序的服务。
* Compose的使用一般分位三步
  * 1.使用Dockerfile 定义应用程序的环境，以便可以在任何地方复制它
  * 2.在docker-compose.yml中定义组成应用程序的服务，以便它们可以在隔离的环境中一起运行
  * 3.运行docker-compose up，然后Compose启动并运行您的整个应用程序
#### Docker-compose安装
* MacOS、Windows系统使用的Docker Desktop默认已经安装
* Linux系统：
  * https://github.com/docker/compose/releases
  * curl "https://github.com/docker/compose/releases/download/1.25.4/docker-compose-`$(uname -s)-`$(uname -m)" -o /usr/local/bin/docker-compose
  * 更改权限：chmod +x /usr/local/bin/docker-compose
  * 查看版本：docker-compose version
## Docker的Registry介绍.md
* https://hub.docker.com/_/registry
* Docker registry 是存储Docker image的仓库，运行push、pull、search时，是通过Docker daemon 与 docker registry 通信。有时候使用 Docker Hub 这样的公共仓库可能不方便，我们可以通过 registry 创建一个本地仓库。
#### 创建本地仓库
* docker run -d -p 5000:5000 -v ${PWD}/registry --restart always --name registry registry:2.7.1
* 查看本地仓库包：本地ip:5000/v2/_catalog
#### 修改远程机器配置
* 进入目录cd /etc/docker
* 修改daemon.json文件
  ```
  {
      "insecure-registries":["192.168.31.60:5000"]
  }
  ```
* 重启docker：systemctl restart docker
#### push到本地仓库
* 重新给镜像打标签：docker tag nginx:1.18.0 本机ip:5000/nginx:1.18.0
* docker push 本机ip:5000/nginx:1.18.0
#### 远程机器pull
* docker pull 本机ip:5000/nginx:1.18.0 
#### 本地build推送到registry
* docker build -t 本地ip:5000/flask-web:1 .
## Dockerfile语法与指令.md
* Dockerfile是由一系列指令和参数构成的脚本，一个Dockerfile里面包含了构建整个镜像的完整命令。通过docker build 执行Dockerfile 中的一系列指令自动构建镜像。
#### 常用命令
* FROM：基础镜像，FROM命令必须是Dockfile的首个命令
* LABEL：为镜像生成元数据标签信息
* USER：指定运行容器时的用户名或者UID，后续RUN也会使用指定用户。
* RUN：RUN命令是Dockerfile执行命令的核心部分。它接受命令作为参数并用户创建镜像。每条RUN命令在当前基础镜像上执行，并且会提交一个新镜像层。
* WORKDIR：设置CMD指明的命令的运行目录。为后续的RUN、CMD、ENRTYPOINT、ADD指令配置工作目录。
* ENV：容器启动的环境变量
* ARG：构建环境的环境变量
* COPY：复制文件
* CMD：容器运行时执行的默认命令。
* ENTRYPOINT：指定容器的"入口"。
* HEALTHCHECK：容器健康状态检查
## Docker镜像构建.md
#### 简介
* 在日常的工作中，尝尝需要制作自己的项目的镜像，一般通过一下两种方式制作镜像：Docker commit、Dockerfile。
#### Docker commit
* Docker commit 一般用作从一个运行状态的容器来创建一个新的镜像。定制镜像应该使用 Dockerfile 来完成。默认 commit 镜像，对外不可解释，不方便排查问题，可维护性差。
* docker commit 容器名 新镜像名:tag
#### Docker build
* 忽略文件：.dockerignore
* 指定文件：docker build -f
* 添加标签 docker build -t
* 不使用缓存：docker build --no-cache
* 构建时变量：docker build --build-arg
  * ARG 指定变量
## Docker实战常用测试平台搭建 
#### 安装私有镜像仓库
* docker pull registry:2
* docker run -d -p 5000:5000 -v /usr/local/registry:/var/lib/registry --restart=always --name registry registry:2
* vim dockerimage.sh创建一个运行docker的sh脚本
  ```
  rm -f registry
  docker run -d -p 5000:5000 -v /usr/local/registry:/var/lib/registry --restart=always --name=registry registry:2
  ```
* bash dockerimages.sh 运行脚本启动registry
* docker tag busybox localhost:5000/busybox:v1.0
* docker push localhost:5000/busybox:v1.0
* curl http://localhost:5000/v2/_catalog
#### 绕过https认证的方式
{"registry-mirrors":["https://registry.docker-cn.com"]}
#### 为什么不能用docker commit来制作镜像
* 制作镜像的方式不可跟踪不可记录不可回溯不可扩展，就是因为dockerfile的出现。docker才流行起来
* Dockerfile文件单独放一个文件夹，因为build的时候需要把Dockerfile文件所在文件夹发送到docker daemon进程上
#### Dockerfile镜像文件组成
* FROM 命令，集成基础镜像-- FROM centos:7
* ADD 命令，把启动脚本或者外部文件加入镜像 -- ADD entrypont.sh /root
* RUN 命令，定义shell命令 -- 
  * RUN yum install -y wget git
  * RUN yum install -y wget
  * RUN yum install -y git
  * RUN yum install -y openssh-server openssl
  * RUN yum install -y vim
* ENTRYPOINT 命令，容器启动脚本--ENTRYPOINT ["/bin/bash","/root/entrypoint.sh"] 使用bash命令执行entrypoint脚本
* EVN 命令，给镜像指定环境变量 -- ENV JAVA_HOME =/opt/java-1.8
  #### 构建镜像
* docker build -t localhost:5000/mynewimage:v1.0 . 默认找当前目录下的Dockerfile文件;-t 命名镜像，仓库地址:端口号/. 镜像名:版本号;加上工作目录（上下文）
#### 多个RUN和一个RUN哪个方式好
* 在编写调试过程中，分着写RUN
  * 缓存，每次RUN都会加载到缓存中，修改RUN指令会重新执行一次RUN不走缓存
  * docker 是分层镜像系统，是按RUN指令来分层管理的，一个RUN指令一层
* 在文件编写确认完成后，合并成一个RUN指令
  * 分层的问题是会带来IO的损耗
#### Docker 文件系统
* 联合文件系统AUFS，一个目录下看到所有原不同目录下的文件
  * 容器层--可读可写
  * 镜像层--只读
  * 视图层--我们看到的
* 分层可以重复利用










   































