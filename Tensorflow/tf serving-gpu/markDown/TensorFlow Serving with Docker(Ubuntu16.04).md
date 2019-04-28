# TensorFlow Serving with Docker

## 1.Ubuntu16.04下安装Docker CE

1.卸载旧版本的Docker：

```python
sudo apt-get remove docker docker-engine docker.io
```

2.安装可选内核模块包以使用 AUFS：

```python
sudo apt-get update
sudo apt-get install  linux-image-extra-$(uname -r)  linux-image-extra-virtual
```

3.添加使用HTTPS 传输的软件包以及 CA 证书：

```python
sudo apt-get update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
```

4.确认所下载软件包的合法性，需要添加软件源的 GPG 密钥(强烈建议国内源)：

```python
curl -fsSL https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
# 官方源
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

5.向 source.list 中添加 Docker 软件源：

```python
sudo add-apt-repository \
"deb [arch=amd64] https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu \
$(lsb_release -cs) \
stable"
 
# 官方源
#  sudo add-apt-repository \
# "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
# $(lsb_release -cs) \
# stable
```

6.更新 apt 软件包缓存，并安装 Docker CE：

```python
sudo apt-get update
sudo apt-get install docker-ce
```

7.启动Docker CE：

```python
sudo systemctl enable docker
sudo systemctl start docker
```

8.测试安装是否正确：

```python
sudo docker run hello-world

# 返回结果
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
ca4f61b1923c: Pull complete
Digest: sha256:445b2fe9afea8b4aa0b2f27fe49dd6ad130dfe7a8fd0832be5de99625dad47cd
Status: Downloaded newer image for hello-world:latest
 
Hello from Docker!
This message shows that your installation appears to be working correctly.
 
To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.
 
To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash
 
Share images, automate workflows, and more with a free Docker ID:
 https://cloud.docker.com/
 
For more examples and ideas, visit:
 https://docs.docker.com/engine/userguide/
```

出现上述信息表示安装正确！



## 2.安装Tensorflow Model Server

1.安装依赖：

```python
apt-get install -y python3 build-essential curl libcurl3-dev git libfreetype6-dev libzmq3-dev pkg-config python3-dev python3-numpy python3-pip software-properties-common swig zip zlib1g-dev
```

 2.配置python环境：

```python
ln -s /usr/bin/python3 /usr/bin/python
ln -s /usr/bin/pip3 /usr/bin/pip
```

3.安装tensorflow-serving-api：

```python
pip install tensorflow-serving-api
```

4.配置tensorflow-model-server仓库：

```python
echo "deb [arch=amd64] http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" | tee /etc/apt/sources.list.d/tensorflow-serving.list

curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | apt-key add -
```

5.安装tensorflow-model-server

```python
apt-get remove tensorflow-model-server
apt-get install tensorflow-model-server
```



## 3.安装NVIDIA显卡驱动

1.英伟达官网下载驱动程序(http://www.nvidia.cn/Download/index.aspx?lang=cn)

   注意：下载Linux版本，以.run结尾的文件格式（建议410版本以上）。

2.禁用nouveau第三方驱动，在终端（Ctrl-Alt+T）输入：

```python
打开编辑配置文件： sudo gedit /etc/modprobe.d/blacklist.conf

最后一行添加：blacklist nouveau

改好后执行命令：sudo update-initramfs -u

重启使之生效：reboot
```

3.安装驱动，重启后在终端（Ctrl-Alt+T）执行命令：

```python
lsmod | grep nouveau
```

  3-1   禁用X服务：

```python
sudo /etc/init.d/lightdm stop
或
sudo service lightdm stop
```

  3-2   找到驱动文件NVIDIA-Linux-x86_64-xxx.xx.run所在目录，给驱动run文件赋予可执行权限，进入该目录：

```python
sudo chmod a+x NVIDIA-Linux-x86_64-xxx.xx.run
```

  3-3   安装驱动文件：

```python
sudo ./NVIDIA-Linux-x86_64-xxx.xx.run -no-opengl-files  # 注:在.run文件所在目录安装
```

  3-4   开启X服务：

```python
sudo /etc/init.d/lightdm start
或
sudo service lightdm start
```

完成安装后重启。



## 4.安装NVIDIA CUDA Toolkit 10.0

1.Ctrl-Alt+F1进入命令行界面之后输入用户名和密码登录，找到cuda_xx_linux.run所在目录（默认为当前用户的

   Downloads目录下）并赋予给文件可执行权限，并进行安装：

```python
cd Downloads
sudo chmod a+x cuda_xxx.run
sudo service lightdm stop   #关闭图形界面
sudo ./cuda_xx.x_linux.run
```

注意：安装过程中当询问是否安装显卡驱动时选n，因为先前已安装完显卡驱动无需再进行安装。

2.设置环境变量：

```python
sudo service lightdm start   #开启图形界面
```

3.登录系统，打开终端（Ctrl-Alt+T）：

```python
sudo gedit /etc/profile
```

在文件最后添加：

```python
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-10.0/lib64
export PATH=$PATH:/usr/local/cuda-10.0/bin
export CUDA_HOME=$CUDA_HOME:/usr/local/cuda-10.0
```

4.保存退出，打开终端：

```python
source /etc/profile   # 运行生效
```

5.验证CUDA是否安装成功：

```python
nvcc -V   # 出现版本号信息即成功
```



## 5.Docker部署官方现有tf serving模型

1.拉取最新TensorFlow Serving GPU的Docker镜像：

```python
docker pull tensorflow/serving:latest-gpu
sudo docker images 	  # 查询Docker镜像
```

2.创建临时目录，并进入该目录，clone官方现有模型：

```
mkdir -p /tmp/tfserving
cd /tmp/tfserving
git clone https://github.com/tensorflow/serving
```

3.使用Docker命令启动服务：启动REST API并监听8501端口，该操作会启动TensorFlow Model Server，	

   并将REST API绑定到8501端口上，同时将模型映射到Docker容器对应的位置：

```python
docker run --runtime=nvidia -p 8501:8501 \
  --mount type=bind,\
  source=/tmp/tfserving/serving/tensorflow_serving/servables/tensorflow/testdata/saved_model_half_plus_two_gpu,\
  target=/models/half_plus_two \
  -e MODEL_NAME=half_plus_two -t tensorflow/serving:latest-gpu &
    
# --mount：   表示要进行挂载
# source：    指定要运行部署的模型地址， 也就是挂载的源，这个是在宿主机上的模型目录
# target:     这个是要挂载的目标位置，也就是挂载到docker容器中的哪个位置，这是docker容器中的目录
# -t:         指定的是挂载到哪个容器
# -p:         指定主机到docker容器的端口映射
# docker run: 启动这个容器并启动模型服务
# 综合解释：
         # 将source目录中的例子模型，挂载到-t指定的docker容器中的target目录，并启动
# 注意：如果执行报错无法识别type=bind， 那应该是source的路径有问题
```

注：<1>若Docker命令启动报如下错：" invalid argument 'type=bind...' "：

​	       解决方法：命令行target、source等参数前不能有空格，将多出的空格删除即可。

​	<2>如果报错信息显示端口port被占，解决方法：

```python
sudo docker ps -a    # 查询Docker容器
sudo docker rm -f 容器ID    # 删除占用端口的容器，并重新启动服务即可
```

4.模型部署成功之前，等2-3s，当出现以下信息表明部署成功：

```python
2018-07-27 00:07:20.773693: I tensorflow_serving/model_servers/main.cc:333]
Exporting HTTP/REST API at:localhost:8501 ...
```

如果没有反应，重新启动Docker：

```python
sudo systemctl start docker

# 如果仍没有反应：
sudo docker ps -a   # 输入登录密码之后，重新使用Docker命令启动服务即可
```

5.使用模型预测结果：

```python
$ curl -d '{"instances": [1.0, 2.0, 5.0]}' \
  -X POST http://localhost:8501/v1/models/half_plus_two:predict
```

返回值为：

```python
{ "predictions": [2.5, 3.0, 4.5] }   # 模型预测值
```



## 6.Docker部署tf serving（替换官网模型）

1.在指定路径下存放已完成训练的模型文件，以facenet模型为例（e.g：默认当前路径为/home/tf-serving）

```python
$ mkdir facenet
$ cd facenet
$ mkdir 00000123
$ cd 00000123
```

进入00000123目录之后，通过FileZilla或者WinSCP软件，连接服务器，将自己训练好的.pb模型放入该目录下，

模型目录结构为：

```python
── 00000123
   ├── saved_model.pb
   └── variables  # 文件夹内为参数及权重文件
       ├── variables.data-00000-of-00001
       └── variables.index
```

注：tf serving希望读取的pb模型是SavedModel.pb格式的，实际有些模型的格式为FrozenModel.pb，这就需要

​        通过相关代码，对pb模型的格式进行转化；或者直接将模型保存为SavedModel.pb格式。

2.进入facenet目录，更换模型路径，输入Docker命令并启动服务：

```python
docker run --runtime=nvidia -p 8501:8501 \
  --mount type=bind,\
  source=/home/tf-serving/facenet,\
  target=/models/facenet \
  -e MODEL_NAME=facenet -t tensorflow/serving:latest-gpu &
```

注：在输入命令时，source、target等参数前去掉多余空格。

3.等待2-3s，当出现如下信息，表示部署模型成功：

```python
2018-07-27 00:07:20.773693: I tensorflow_serving/model_servers/main.cc:333]
Exporting HTTP/REST API at:localhost:8501 ...
```

