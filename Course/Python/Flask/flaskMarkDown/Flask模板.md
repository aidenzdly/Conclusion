## Flask模板

Flask可以以HTML形式返回绑定到某个URL的函数的输出。 例如，在以下脚本中，`hello()`函数将使用附加的`<h1>`标记呈现*‘Hello World’* 。

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<html><body><h1>'Hello World'</h1></body></html>'

if __name__ == '__main__':
    app.run(debug = True)
```

但是，从Python代码生成HTML内容非常麻烦，尤其是在需要放置可变数据和Python语言元素(如条件或循环)时。经常需要转义HTML代码。

它可以利用Jinja2模板引擎技术，而不需要从函数返回硬编码HTML。如下代码所示，可以通过`render_template()`函数渲染HTML文件。

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
   return render_template(‘hello.html’)

if __name__ == '__main__':
   app.run(debug = True)
```

Flask将尝试在该脚本所在的同一文件夹中查找`templates`文件夹中的HTML文件。使用模板的应用程序目录结构如下所示 -

```python
app.py
hello.py
    templates
        hello.html
        register.html
        ....
```

术语“Web模板系统”是指设计一个HTML脚本，其中可以动态插入变量数据。 Web模板系统由模板引擎，某种数据源和模板处理器组成。

Flask使用jinga2模板引擎。 Web模板包含用于变量和表达式(这些情况下为Python表达式)的HTML语法散布占位符，这些变量和表达式在模板呈现时被替换为值。

以下代码在模板(*templates*)文件夹中保存为:*hello.html*。

```python
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Flask HTTP请求方法处理</title>
</head>
   <body>

      <h1>Hello {{ name }}!</h1>

   </body>
</html>
```

接下来，将以下代码保存在*app.py*文件中，并从Python shell运行 -

```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name = user)

if __name__ == '__main__':
    app.run(debug = True)
```

在开发服务器开始运行时，打开浏览器并输入URL为 - `http://localhost:5000/hello/maxsu`

URL的可变部分插入`{{name}}`占位符处。

![2123](C:\Users\T470P\Desktop\2123.png)

Jinja2模板引擎使用以下分隔符来从HTML转义。

`{% ... %}` 用于多行语句

`{{ ... }}` 用于将表达式打印输出到模板

`{# ... #}` 用于未包含在模板输出中的注释

`# ... ##` 用于单行语句

在以下示例中，演示了在模板中使用条件语句。 `hello()`函数的URL规则接受整数参数。 它传递给`hello.html`模板。 在它里面，收到的数字(标记)的值被比较(大于或小于50)，因此在HTML执行了有条件渲染输出。

Python脚本如下 -

```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<int:score>')
def hello_name(score):
    return render_template('hello.html', marks = score)

if __name__ == '__main__':
    app.run(debug = True)
```

模板文件:*hello.html* 的HTML模板脚本如下 -

```python
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Flask模板示例</title>
</head>
   <body>

      {% if marks>50 %}
      <h1> 通过考试！</h1>
      {% else %}
      <h1>未通过考试！</h1>
      {% endif %}

   </body>
</html>
```

请注意，条件语句`if-else`和`endif`包含在分隔符`{%..。%}`中。

运行Python脚本并访问URL=> `http://localhost/hello/60` ，然后访问 `http://localhost/hello/59`，以有条件地查看HTML输出。

Python循环结构也可以在模板内部使用。 在以下脚本中，当在浏览器中打开URL => `http:// localhost:5000/result`时，`result()`函数将字典对象发送到模板文件:*results.html* 。

*result.html* 的模板部分采用for循环将字典对象`result{}`的键和值对呈现为HTML表格的单元格。

从Python shell运行以下代码。

```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')
def result():
    dict = {'phy':59,'che':60,'maths':90}
    return render_template('result.html', result = dict)

if __name__ == '__main__':
    app.run(debug = True)
```

将以下HTML脚本保存为模板文件夹(*templates*)中的模板文件:*result.html* 。

```python
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Flask模板示例</title>
</head>
   <body>
      <table border = 1>
         {% for key, value in result.items() %}
            <tr>
               <th> {{ key }} </th>
               <td> {{ value }} </td>
            </tr>
         {% endfor %}
      </table>
   </body>
</html>
```

在这里，与For循环相对应的Python语句包含在`{%...%}`中，而表达式键和值放在`{{}}`中。

开发开始运行后，在浏览器中打开`http://localhost:5000/result`以获得以下输出。

![223](C:\Users\T470P\Desktop\223.png)

