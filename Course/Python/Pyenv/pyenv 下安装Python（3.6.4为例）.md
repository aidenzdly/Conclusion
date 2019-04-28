## pyenv 下安装Python（3.6.4为例）

##### 1.将要安装的python版本的tar.xz格式的源码包提前下载好放置`~/.pyenv/cache`目录下，没有cache文件夹则创建

```python
  mkdir ~/.pyenv/cache
  wget -P ~/.pyenv/cache https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tar.xz
```

##### 2.安装依赖(python3.X 通用)

```python
Ubuntu：
sudo apt-get install build-essential python-dev python-setuptools python-pip python-smbus build-essential libncursesw5-dev libgdbm-dev libc6-dev zlib1g-dev libsqlite3-dev tk-dev libssl-dev openssl libffi-dev libssl-dev zlib1g-dev libbz2-dev libreadline-dev xz-utils liblzma-dev python-openssl -y

Centos：
sudo yum install zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel libffi-devel

```

##### 3.使用`pyenv install <version> `命令进行安装

```python
pyenv install 3.6.4

# 若报错尝试删除/tmp目录下与python相关的文件
```

##### 4.将全局Python版本设置为3.6.4

```python
pyenv global 3.6.4
```

##### 

#### 重启Terminal 输入python -V若输出3.6.4则代表配置成功！！