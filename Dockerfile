# 使用Python基础镜像
FROM python:3.7-slim

# 安装Python包管理工具和依赖
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    && apt-get clean

# 安装Google Chrome浏览器
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update && apt-get install -y google-chrome-stable

# 安装ChromeDriver
RUN wget -O /tmp/chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.141/linux64/chromedriver-linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/

# 安装Python依赖包
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# 复制测试脚本到容器中
COPY . /app

# 设置工作目录
WORKDIR /app

# 运行测试脚本
CMD ["pytest", "-vs", "test_demo.py"]
