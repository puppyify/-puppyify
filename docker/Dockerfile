# 使用Python 3.10作为基础镜像
FROM python:3.10

LABEL maintainer="puppyify@163.com"
LABEL version="0.1.0"

# 安装Git工具
RUN apt-get update && \
    apt-get install -y git

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到容器的/app目录中
COPY server/ /app/

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

ENV PUPPYIFY_PATH '/var/puppyify'

EXPOSE 8888

# 设置入口命令
ENTRYPOINT python -u app.py
