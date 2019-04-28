## Flask重定向和错误

Flask类有重定向`redirect()`函数。调用时，它会返回一个响应对象，并将用户重定向到具有指定状态码的另一个目标位置。

`redirect()`函数的原型如下 -

```
Flask.redirect(location, statuscode, response)
```

在上述函数中 -

- *location* 参数是响应应该被重定向的URL。
- *statuscode* 参数发送到浏览器的头标，默认为`302`。
- *response* 参数用于实例化响应。

以下状态代码是标准化的 -

- HTTP_300_MULTIPLE_CHOICES
- HTTP_301_MOVED_PERMANENTLY
- HTTP_302_FOUND
- HTTP_303_SEE_OTHER
- HTTP_304_NOT_MODIFIED
- HTTP_305_USE_PROXY
- HTTP_306_RESERVED
- HTTP_307_TEMPORARY_REDIRECT

默认状态码是`302`，这是表示’找到’页面。

在以下示例中，`redirect()`函数用于在登录尝试失败时再次显示登录页面。

```python
from flask import Flask, redirect, url_for, render_template, request
# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('log_in.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST' and
        request.form['username'] == 'admin' :
        return redirect(url_for('success'))
    return redirect(url_for('index'))

@app.route('/success')
def success():
    return 'logged in successfully'

if __name__ == '__main__':
    app.run(debug = True)
```

Flask类具有带有错误代码的`abort()`函数。

```python
Flask.absort(code)
```

`code`参数使用以下值之一 -

- 400 - 对于错误的请求
- 401 - 用于未经身份验证
- 403 - 禁止
- 404 - 未找到
- 406 - 不可接受
- 415 - 用于不支持的媒体类型
- 429 - 请求过多

这里对上面的代码中的`login()`函数进行一些细微的修改。 如果要显示“Unauthourized”页面，而不是重新显示登录页面，请将其替换为中止(401)的调用。

```python
from flask import Flask, redirect, url_for, render_template, request, abort
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('log_in.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' :
            return redirect(url_for('success'))
        else:
            abort(401)
    else:
        return redirect(url_for('index'))

@app.route('/success')
def success():
    return 'logged in successfully'

if __name__ == '__main__':
    app.run(debug = True)
```

