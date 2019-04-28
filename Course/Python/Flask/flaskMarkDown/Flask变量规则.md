## Flask变量规则

可以通过将可变部分添加到规则参数来动态构建URL。 这个变量部分被标记为`<variable-name>`。 它作为关键字参数传递给规则所关联的函数。

在以下示例中，`route()`装饰器的规则参数包含附加到URL `/hello`的`<name>`变量部分。 因此，如果在浏览器中输入URL: `http://localhost:5000/hello/YiibaiYiibai`，那么 ‘YiibaiYiibai’ 将作为参数提供给`hello()`函数。

参考如下代码 -

```python
from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')  #输入url时添加参数<name>
def hello_name(name):
    return 'Hello %s!' % name

if __name__ == '__main__':
    app.run(debug = True）
```

将上面的脚本保存到文件:`hello.py`，并从Python shell运行它。

![333](C:\Users\T470P\Desktop\333.png)

接下来，打开浏览器并输入URL => `http://localhost:5000/hello/YiibaiYiibai`。在浏览器中输出如下所示 -

![444](C:\Users\T470P\Desktop\444.png)

除了默认的字符串变量部分之外，还可以使用以下转换器构造规则 -

| 编号   | 转换器   | 描述               |
| ---- | ----- | ---------------- |
| 1    | int   | 接受整数             |
| 2    | float | 对于浮点值            |
| 3    | path  | 接受用作目录分隔符的斜杠符（/） |

在下面的代码中，使用了所有这些构造函数。

```python
from flask import Flask
app = Flask(__name__)

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' % revNo

if __name__ == '__main__':
    app.run()
```

从Python Shell运行上述代码。 在浏览器中访问URL => `http:// localhost:5000/blog/11`。

给定的数字值作为:`show_blog()`函数的参数。 浏览器显示以下输出 -

```python
值：  Blog Number 11
```



在浏览器中输入此URL - `http://localhost:5000/rev/1.1`

`revision()`函数将浮点数作为参数。 以下结果出现在浏览器窗口中 -

```python
值：  Revision Number 1.100000
```



Flask的URL规则基于Werkzeug的路由模块。 这确保了形成的URL是唯一的，并且基于Apache制定的先例。

考虑以下脚本中定义的规则 -

```python
from flask import Flask
app = Flask(__name__)

@app.route('/flask')
def hello_flask():
    return 'Hello Flask'

@app.route('/python/')
def hello_python():
    return 'Hello Python'

if __name__ == '__main__':
    app.run()
```

两条规则看起来都很相似，但在第二条规则中，使用了尾部斜线(`/`)。 因此，它变成了一个规范的URL。 因此，使用`/python`或`/python/`返回相同的输出。 但是，在第一条规则的情况下， URL:`/flask/`会导致`404 Not Found`页面。