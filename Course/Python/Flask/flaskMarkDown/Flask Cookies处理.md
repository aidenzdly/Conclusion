## Flask Cookies处理

Cookie以文本文件的形式存储在客户端计算机上。 其目的是记住和跟踪与客户使用有关的数据，以获得更好的访问体验和网站统计。

Request对象包含一个`cookie`的属性。 它是所有cookie变量及其对应值的字典对象，客户端已发送。 除此之外，cookie还会存储其到期时间，路径和站点的域名。

在Flask中，cookies设置在响应对象上。 使用`make_response()`函数从视图函数的返回值中获取响应对象。 之后，使用响应对象的`set_cookie()`函数来存储cookie。

重读cookie很容易。 可以使用`request.cookies`属性的`get()`方法来读取cookie。

在下面的Flask应用程序中，当访问URL => `/` 时，会打开一个简单的表单。

```python
@app.route('/')
def index():
    return render_template('index.html')
```

这个HTML页面包含一个文本输入，完整代码如下所示 -

```python
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Flask Cookies示例</title>
</head>
   <body>

      <form action = "/setcookie" method = "POST">
         <p><h3>Enter userID</h3></p>
         <p><input type = 'text' name = 'name'/></p>
         <p><input type = 'submit' value = '登录'/></p>
      </form>

   </body>
</html>
```

表单提交到URL => `/setcookie`。 关联的视图函数设置一个Cookie名称为:`userID`，并的另一个页面中呈现。

```python
@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
        user = request.form['name']

        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)

        return resp
```

`readcookie.html` 包含超链接到另一个函数`getcookie()`的视图，该函数读回并在浏览器中显示cookie值。

```python
@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome '+name+'</h1>'
```

下列为readcookie.html -

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
cookie已经设置完成
请点击<a href="{{ url_for('getcookie') }}">这里</a>查看
</body>
</html>
```



完整的应用程序代码如下 -

```python
from flask import Flask
from flask import render_template
from flask import request
from flask import make_response


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['name']

        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)
        return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    print (name)
    return '<h1>welcome, '+name+'</h1>'

if __name__ == '__main__':
    app.run(debug = True)
```

运行该应用程序并访问URL => `http://localhost:5000/`

![ss4](C:\Users\T470P\Desktop\ss4.png)

设置cookie的结果如下所示 -

![11a0](C:\Users\T470P\Desktop\11a0.png)

重读cookie的输出如下所示 -

![2239](C:\Users\T470P\Desktop\2239.png)

