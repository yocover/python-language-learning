FROM ubuntu:22.04

# 设置时区为上海
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 更新包列表并安装基本工具和 SSH 服务
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    vim \
    git \
    openssh-server \
    && rm -rf /var/lib/apt/lists/*

# 创建 SSH 所需目录
RUN mkdir /var/run/sshd

# 设置 root 密码
RUN echo 'root:password' | chpasswd

# 允许 root 用户 SSH 登录
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH 登录时需要的环境变量
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# 设置工作目录
WORKDIR /workspace

# 暴露 SSH 端口
EXPOSE 22

# 启动 SSH 服务
CMD ["/usr/sbin/sshd", "-D"] 