部署TensorFlow Serving-GPU时，采用最简单的方法Docker部署。在Ubuntu16.04环境下，部署之前，首先需要安装Docker CE，安装时，要卸载旧版本的Docker，安装证书，添加GPG 密钥以及Docker 软件源等相关依赖，然后执行Docker CE安装命令，完成启动及测试。

其次，需要安装Tensorflow Model Server，便于统一管理一个模型服务器，利于让他人使用这个模型，而且可以动态更新模型，模型也会常住在内存里面，加快结果输出，减少模型加载时间。安装依赖包及tf serving-api，配置python环境以及Tensorflow Model Server仓库，执行安装命令并完成启动测试。

接着在NVIDIA官网下载Linux版本的显卡驱动(.run结尾，版本最好为410以上)，禁用第三方驱动及服务，安装驱动，在对应目录下赋予可执行权限并安装.run驱动文件，安装完成之后重新启动即可。

之后安装NVIDIA CUDA Toolkit 10.0，在官网下载Linux版本.run文件之后，设置环境变量，修改配置文件保存并退出，输入命令nvcc -V测试安装是否成功。

最后准备工作完成之后，开始使用Docker部署模型，首先我们需要拉取最新的TensorFlow Serving-GPU的镜像文件，拉取完成之后，创建模型目录并进入，clone官方模型。接着使用Docker命令启动服务：启动REST API并监听8501端口，该操作会启动TensorFlow Model Server，并将REST API绑定到8501端口上，同时将模型映射到Docker容器对应的位置，等待2-3s，模型部署成功。若无反应，重启Docker，输入密码启动服务。

