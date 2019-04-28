# Flask + uWSGI + Nginx部署

### 1.配置:

- 服务器: 1核1G基础服务器
- 操作系统: UBuntu16.04LTS
- 部署框架: `Nginx`, `uWSGI`
- `python`: `python3.6`

### 2.Venv-install

#### 2-1   安装

###### 	2-1-1   将 pyenv 检出到你想安装的目录。建议路径为： `$HOME/.pyenv` 	

```python
		cd ~

		git clone git://github.com/yyuu/pyenv.git .pyenv
```

###### 	2-1-2   添加环境变量。`PYENV_ROOT`指向 pyenv 检出的根目录，并向 `$PATH` ;添加 `PYENV_ROOT/bin` 以提供访问 `pyenv`这条命令的路径	

```python
		echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
		echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
        
        注：这里的 shell 配置文件（~/.bash_profile）依不同 Linux 而需作修改——Zsh：~/.zshenv；Ubuntu：~/.bashrc
```

###### 	2-1-3   向 shell 添加 `pyenv init` 以启用 shims 和命令补完功能		

```；python
		echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
    
    	注：这里的 shell 配置文件（~/.bash_profile）依不同 Linux 而需作修改——Zsh：~/.zshenv；Ubuntu：~/.bashrc
```

###### 	2-1-4   重启 shell（因为修改了 `$PATH` ）	

```python
		exec $SHELL
```

#####       命令使用		

```python
	pyenv install --list   # 列出可安装版本

	pyenv install <version>   # 安装对应版本

	pyenv install -v <version>   # 安装对应版本，若发生错误，可以显示详细的错误信息

	pyenv versions   # 显示当前使用的python版本

	pyenv which python   # 显示当前python安装路径

	pyenv global <version>  # 设置默认Python版本

	pyenv local <version>   # 当前路径创建一个.python-version, 以后进入这个目录自动切换为该版本

	pyenv shell <version>   # 当前shell的session中启用某版本，优先级高于global 及 local
```

#### 2-2   使用虚拟环境

######       安装

```python
	<1>查看pyenv-virtualenv到插件目录

	   $ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv	
```

```python
 	<2>（可选）添加pyenv virtualenv-init到shell以启用virtualenvs的自动激活
    
       $ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
    
    注：这里的 shell 配置文件（~/.bash_profile）依不同 Linux 而需作修改——Zsh：~/.zshenv；Ubuntu：~/.bashrc
    
    <3>重新启动shell以启用pyenv-virtualenv
    	
        $ exec  $SHELL
     
```

### 3.安装Nginx

```python
    sudo apt-get install nginx
    # 剩下的还有`uWSGI`没有安装,这个最好在虚拟环境下安装,但是由于`uWSGI`十个一基于C语言的框架,还需要安装他的依赖包
    
    
    # 因为我使用的是 Python3 所以这里安装的是 Python3 的依赖包
	sudo apt-get install build-essential python3-dev

	# 如果报错可以试着安装这个
	（sudo apt-get install build-essential python-dev）
    
    # 安装完uWSGI的依赖包之后，创建虚拟环境
    
	<1>从默认版本创建虚拟环境

	   pyenv virtualenv env
    
    <2>创建3.6版本的虚拟环境 
    
       pyenv virtualenv 3.6.4 env-3.6.4  

    <3>激活虚拟环境

	   pyenv activate env-3.6.4

    <4>关闭（退出)虚拟环境

	   pyenv deactivate

    #<5>自动激活

     # 使用pyenv local 虚拟环境名
    
     # 会把`虚拟环境名`写入当前目录的.python-version文件中
    
     # 关闭自动激活 -> pyenv deactivate
    
     # 启动自动激活 -> pyenv activate env-3.6.4
    
     pyenv local env-3.6.4

    #<6>删除
    
     pyenv uninstall env-3.6.4 
        
```

### 4.安装uWSGI

######    进入虚拟环境之后（pyevn-3.6.4），安装uwsgi（在虚拟环境中安装）

```python
   (pyevn-3.6.4)pip install uwsgi
```



### 5.环境配置

```python
	# 创建目录，创建py文件（或项目），拟定nginx、uwsgi配置文件

	$ mkdir my_flask_app
	$ cd my_flask_app
	$ touch hello.py
	$ touch run.py
	$ touch helloflask_nginx.conf  #nginx 配置文件
	$ touch helloflask_uwsgi.ini   #uwsgi 配置文件
————————————————————————————————————————————
    
```

```python
# hello.py`文件内容如下:
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
————————————————————————————————————————————    
    
# run.py 文件内容如下:
from hello import app

if __name__ == '__main__' :
        app.run(host='0.0.0.0',port=5001)
————————————————————————————————————————————        
        
# helloflask_nginx.conf文件内容如下:
server {
    listen 80;    					    
    server_name xxx.xxx.xx.xxx;		# 服务器公网ip

    location / {
        include uwsgi_params;			#uwsgi 需要参数,不需要改动
        uwsgi_pass 127.0.0.1:3031;   
    }
}

# 参数意义：

  # listen: 监听端口 80(默认)
       
  # server_name: 部署服务器ip地址,或者域名
    
  # uwsgi_pass : Nginx 与 uwsgi本地通讯地址
    
————————————————————————————————————————————

# helloflask_uwsgi.ini文件内容如下:
[uwsgi]
master = true
home = /home/ubuntu/my_flask_app/venv    
chdir = /home/ubuntu/my_flask_app	       
wsgi-file = run.py							
callable = app								
socket = 127.0.0.1:3031						
processes = 4									
threads = 2						
buffer-size = 32768							
stats = 127.0.0.1:9091	
    
# 参数意义：

   # home : 虚拟环境路径（重要：找到与创建虚拟环境一致的python版本）
    
   # chdir: 项目文件路径

   # wsgi-file: 项目启动文件
    
   # callable: 项目启动实例,这个项目就是app = Flask(__name__)里面的这个 app

   # socket: Nginx 与 uwsgi本地通讯地址
    
   # processes:进程数

   # buffer-size:缓存大小
    
   # stats :状态检测地址

——————————————————————————————————————————————
```

`helloflask_nginx.conf`文件中需要重点介绍的是`uwsgi_pass`,也是配置成功的重点,这个是地方的地址,需要与`helloflask_uwsgi.ini`文件中的`socket`地址保持一致,这个是他们之间用于通信的端口地址,当然有的教程里面会把这个配置我一个`.sock`文件的样子,这个也是可以的,但我个人还是比较倾向于上面的端口配置。

当一个请求从 app发起后,首先它会通过80端口到达`nginx`,然后`nginx`通过设置的本地端口将请求转发给`uwsgi`,最后由`uwsgi`分发给应用服务器完成请求的处理,实现一个完成的请求流程。



### 6.启动配置

  6-1   首先,删除`nginx`的默认配置文件:具体参数可以查看官方文档,本文仅提供最简单的配置:[传送门](https://www.nginx.com/resources/wiki/start/)

```python
  sudo rm /etc/nginx/sites-enabled/default
```

  6-2  使用软连接将项目配置文件连接到`nginx`的工作目录中

```python
  $ sudo ln -s /home/ubuntu/my_flask_app/helloflask_nginx.conf /etc/nginx/conf.d/
    
  # 注：一定写对nginx.conf的路径，否则找不到该配置文件
```

  6-3  重启 Nginx：

```python
  $ sudo /etc/init.d/nginx restart
    
  # 如果这个时候您刷新自己服务器,浏览器应该会报一个502的错误,这说明nginx已经启动成功
```

  6-4  启动`uwsgi`：

```python
  $ uwsgi --ini helloflask_uwsgi.ini &    #  & 后台运行
```

如果一切顺利,再次刷新,应该可以看到一切的起源`Hello World!`,到此,项目部署完成!恭喜你!！！

注意几点报错：

   1.如果启动uwsgi服务时，页面显示无法连接，考虑软连接的nginx.conf的路径是否正确；

   2.如果出现No moudle name “econdings”：注意python版本（创建虚拟环境与实际global的python版本）

   3.若果出现-- unavailable modifier requested: 0 -报错，刷新一次出现一次，那么需要在uwsgi.ini文件中添加：*plugins = python*，然后以root用户执行：apt-get install uwsgi-plugin-python



### 7.安装Supervisor

```python
 # 如果需要更加稳定,还需要使用Supervisor来监听程序,当它发现uwsgi或者 Nginx挂了会自动将其重启
```

```python
   $ sudo apt-get install supervisor
    
 
# 一般情况,Supervisor 的全局的配置文件位置在
```

```python
  /etc/supervisor/supervisor.conf
  
# 但我们不需要去对其作出改动,添加一个新的配置文件*.conf在该目录:(该项目文件名为:my_flask_supervisor.conf)
  
  /etc/supervisor/conf.d/
——————————————————————————————————————————————————————————————
  
# my_flask_supervisor.conf文件内容如下:
[program:my_flask]
# 启动命令入口
command=/home/ubuntu/my_flask_app/helloflask_uwsgi.ini

# 命令程序所在目录
directory=/home/ubuntu/my_flask_app
#运行命令的用户名
user=root
		
autostart=true
autorestart=true
#日志地址
stdout_logfile=/home/ubuntu/my_flask_app/logs/uwsgi_supervisor.log
——————————————————————————————————————————————————————————————

# 启动服务
$ sudo service supervisor start
#  $ sudo service supervisor stop  停止服务命令
```



import os

app = Flask(__name__)
@app.route("/frame", methods=['POST'])
def get_frame():
    upload_file = request.files['file']
    fileName = upload_file.filename
    filePath = os.path.join('/home/tf-serving/images/'+ fileName)

    if upload_file:
        upload_file.save(filePath)
        return 'upload images successfully!'
    else:
        return 'upload failed!'

import os

app = Flask(__name__)
@app.route("/frame", methods=['POST'])
def get_frame():
    upload_file = request.files['file']
    fileName = upload_file.filename
    filePath = os.path.join('/home/tf-serving/images/'+ fileName)

    if upload_file:
        upload_file.save(filePath)
        return 'upload images successfully!'
    else:
        return 'upload failed!'

