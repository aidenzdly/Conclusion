## Flask HTTP方法

Http协议是万维网数据通信的基础。 它协议定义了从指定URL中检索不同数据的方法。

下表概括了不同的http方法 -

| 编号   | 方法     | 描述                                       |
| ---- | ------ | ---------------------------------------- |
| 1    | GET    | 将数据以未加密的形式发送到服务器，这最常用的方法。                |
| 2    | HEAD   | 与GET相同，但没有响应主体                           |
| 3    | POST   | 用于将HTML表单数据发送到服务器。通过POST方法接收的数据不会被服务器缓存。 |
| 4    | PUT    | 用上传的内容替换目标资源的所有当前表示。                     |
| 5    | DELETE | 删除由URL给出的所有目标资源的所有表示。                    |

默认情况下，Flask路由响应GET请求。 但是，可以通过为`route()`装饰器提供方法参数来更改此首选项。

为了演示在URL路由中使用POST方法，首先创建一个HTML表单并使用POST方法将表单数据发送到URL。

将以下脚本保存到文件:`login.html`

```python
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title>Flask HTTP请求方法处理</title>
</head>
   <body>
      <form action = "http://localhost:5000/login" method = "post">
         <p>输入姓名:</p>
         <p><input type = "text" name = "name" value=""/></p>
         <p><input type = "submit" value = "提交" /></p>
      </form>

   </body>
</html>
```

现在在Python shell中输入以下脚本。

```
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('name')
        return redirect(url_for('success',name = user))

if __name__ == '__main__':
    app.run(debug = True)
```

开发服务器开始运行后，在浏览器中打开`login.html`，在文本字段中输入名称(如:*maxsu* )并单击**提交**![21](C:\Users\T470P\Desktop\21.png)

表单数据被提交到`<form>`标签的`action`属性指定的URL。

`http://localhost:5000/login`被映射到`login()`函数。 由于服务器已通过POST方法接收数据，因此从表单数据获得`'name'`参数的值，通过以下方式-

```python
user = request.form['name]
```

它作为可变部分传递给URL:`/success`。 浏览器在窗口中显示欢迎消息。

![2331](C:\Users\T470P\Desktop\2331.png)



将`login.html`中的方法参数更改为`GET`并在浏览器中再次打开。 在服务器上收到的数据是通过GET方法。 `'name'`参数的值现在通过以下方式获得 -

```python
user = request.args.get('name)
```

这里，`args`是字典对象，它包含一系列表单参数及其对应值。 与之前一样，与`'name'`参数对应的值将传递到URL:`/success`.