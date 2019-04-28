## Flask URL构建

`url_for()`函数对于动态构建特定函数的URL非常有用。 该函数接受函数的名称作为第一个参数，并接受一个或多个关键字参数，每个参数对应于URL的变量部分。

以下脚本演示了使用`url_for()`函数

<u>"url_for"操作对象是函数，而不是route里的路径</u>

```python
from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def user(name):
    if name =='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest = name))

if __name__ == '__main__':
    app.run(debug = True)
```

上面的脚本有一个函数用户(名称)，它接受来自URL的参数值。

`User()`函数检查收到的参数是否与’admin’匹配。 如果匹配，则使用`url_for()`将应用程序重定向到`hello_admin()`函数，否则将该接收的参数作为`guest`参数传递给`hello_guest()`函数。

保存上面的代码到一个文件:*hello.py*，并从Python shell运行。

打开浏览器并输入URL - `http://localhost:5000/user/admin`

浏览器中的应用程序响应输出结果是 -

```python
Hello Admin
```

在浏览器中输入以下URL - `http://localhost:5000/user/mvl`

应用程序响应结果现在变为 -

```python
Hello mvl as Guest
```

