## Flask Sessions会话

与Cookie不同，会话数据存储在服务器上。 会话是客户端登录到服务器并注销的时间间隔。 需要在此会话中进行的数据存储在服务器上的临时目录中。

与每个客户端的会话分配一个会话ID。 会话数据存储在cookie顶部，服务器以加密方式签名。 对于这种加密，Flask应用程序需要一个定义`SECRET_KEY`。

会话对象也是一个包含会话变量和关联值的键值对的字典对象。

例如，要设置`'username'`会话变量，请使用语句 -

```python
Session['username'] = 'admin'
```

要删除会话变量，请使用`pop()`方法。

```python
session.pop('username', None)
```

以下代码是Flask中会话如何工作的简单演示。 URL => `'/'` 提示用户登录，因为会话变量`username`没有设置。

```python
@app.route('/')
def index():
   if 'username' in session:
      username = session['username']
         return 'Logged in as ' + username + '<br>' + \
         "<b><a href = '/logout'>click here to log out</a></b>"
   return "You are not logged in <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"
```

当用户浏览到URL=>`'/login'`时，`login()`函数显示视图，因为它是通过GET方法调用的，所以打开一个登录表单。

表单填写后重新提交到URL=> `/login`，现在会话变量被设置。 应用程序被重定向到URL=> `/`。 这时找到会话变量:`username`。

```python
@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['username']
      return redirect(url_for('index'))
   return '''
   <form action = "" method = "post">
      <p><input type = text name = "username"/></p>
      <p<<input type = submit value = Login/></p>
   </form>
   '''
```

该应用程序还包含一个`logout()`视图函数，它删除’username’会话变量的值。 再次 URL 跳转到 ‘/‘ 显示开始页面。

```python
@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))
```

运行应用程序并访问主页(确保设置应用程序的`secret_key`)。

```python
from flask import Flask, session, redirect, url_for, escape, request
app = Flask(__name__)
app.secret_key = 'any random string’    # secret_key用于加密
```



完整代码如下所示 -

```python
from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import Flask, session, redirect, url_for, escape, request



app = Flask(__name__)
app.secret_key = 'fkdjsafjdkfdlkjfadskjfadskljdsfklj'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return '登录用户名是:' + username + '<br>' + \
                 "<b><a href = '/logout'>点击这里注销</a></b>"


    return "您暂未登录， <br><a href = '/login'></b>" + \
         "点击这里登录</b></a>"



@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))

    return '''
   <form action = "" method = "post">
      <p><input type ="text" name ="username"/></p>
      <p><input type ="submit" value ="登录"/></p>
   </form>
   '''

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug = True)
```



输出将显示如下。点击链接“**点击这里登录**”。

![11223](C:\Users\T470P\Desktop\11223.png)

该链接将被引导至另一个界面。 输入’admin’。

![231](C:\Users\T470P\Desktop\231.png)

屏幕会显示消息“**登录用户名是:admin**”。如下所示 -

![QQ截图20190424171653](C:\Users\T470P\Desktop\QQ截图20190424171653.png)

