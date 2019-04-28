## Flask应用程序

要测试Flask安装是否成功，在编辑器中输入以下代码，并保存到文件:`Hello.py` 中。

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run()

```

在项目中导入`Flask`模块是强制性的。 Flask类的一个对象是WSGI应用程序。

Flask构造函数将当前模块的名称(`__name__`)作为参数。

Flask类的`route()`函数是一个装饰器，它告诉应用程序哪个URL应该调用相关的函数。

```python
app.route(rule,options)
```

- rule 参数表示与该函数绑定的URL。


- options是要转发给底层Rule对象的参数列表。

在上面的例子中，`'/'` URL与`hello_world()`方法绑定。 因此，在浏览器中打开Web服务器的主页时，将呈现此函数的输出。

最后，Flask类的`run()`方法在本地开发服务器上运行应用程序。

```python
app.run(host,port,debug,options)
```

上面方法中的所有参数都是可选的，作用如下表描述说明 -

| 编号   | 参数      | 描述                                       |
| ---- | ------- | ---------------------------------------- |
| 1    | host    | 监听的主机名，默认为127.0.0.1（localhost）；设置为”0.0.0.0”是服务器在外部使用 |
| 2    | port    | 监听的端口号，默认为：5000                          |
| 3    | debug   | 默认为：false；如果设置为：True，则提供调试信息             |
| 4    | options | 被转发到底层的Werkzeug                          |

上面的*hello.py*脚本保存到D盘下(路径为：*D:\hello.py*)，可以从Python shell执行的。使用如下命令 -

```
$ python hello.py
```

![111](C:\Users\T470P\Desktop\111.png)

在浏览器中打开上面的URL(`localhost:5000`)。将会看到有 ‘Hello World’ 消息显示在浏览器中。

![2222](C:\Users\T470P\Desktop\2222.png)

### 调试模式

Flask应用程序通过调用`run()`方法来启动。 但是，当应用程序正在开发中时，应该为代码中的每个更改手动重新启动它。 为了避免这种不便，可以启用调试支持。 如果代码改变，服务器将自动重新加载。 它还将提供一个有用的调试器来跟踪应用程序中的错误(如果有的话)。

在运行或将调试参数传递给`run()`方法之前，通过将应用程序对象的调试属性设置为`True`来启用调试模式。

```python
app.debug = True
app.run()
app.run(debug = True)

```

