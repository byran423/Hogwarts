FROM python:3.7-alpine
LABEL maintainer="hogwarts"

# 工作路径设定为/Code/tmp
WORKDIR /Code/tmp

# 创建环境变量给Flask 使用
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

# 复制 app.py 到容器内 /Code/tmp 目录
COPY app.py /Code/tmp

# 安装gcc 工具、python的依赖
RUN pip install flask && pip install redis

# 映射端口
EXPOSE 5000

STOPSIGNAL SIGTERM

# 为容器设置默认启动命令
CMD ["flask","run"]


