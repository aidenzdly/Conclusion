## Flask WTF

Web应用程序的一个重要方面是为用户提供一个用户界面。 HTML提供了一个`<form>`标签，用于设计一个接口。 可以适当使用表单的元素，如文本输入，广播，选择等。

通过`GET`或`POST`方法将用户输入的数据以Http请求消息的形式提交给服务器端脚本。

- 服务器端脚本必须从http请求数据重新创建表单元素。 所以实际上，表单元素必须被定义两次 - 一次是HTML，一次是服务器端脚本。
- 使用HTML表单的另一个缺点是很难(如果不是不可能)动态地呈现表单元素。 HTML本身无法验证用户的输入。

这就是`WTForms`，一个灵活的表单，渲染和验证库来得方便的地方。 Flask-WTF扩展为这个WTForms库提供了一个简单的接口。

使用Flask-WTF，可以在Python脚本中定义表单域并使用HTML模板来呈现它们。 也可以将验证应用于WTF字段。

下面让我们看看这个动态生成HTML是如何工作的。

首先，需要安装Flask-WTF扩展。

```python
pip install flask-WTF
```

已安装的软件包包含一个Form类，该类必须用作用户定义表单的父级。WTforms包包含各种表单域的定义。下面列出了一些标准表单字段。

| 编号 | 标准表单字段  | 描述                                      |
| ---- | ------------- | ----------------------------------------- |
| 1    | TextField     | 表示<input type ='text'> HTML表单元素     |
| 2    | BooleanField  | 表示<input type ='checkbox'> HTML表单元素 |
| 3    | DecimalField  | 用小数显示数字的文本字段                  |
| 4    | IntegerField  | 用于显示整数的文本字段                    |
| 5    | RadioField    | 表示<input type ='radio'>的HTML表单元素   |
| 6    | SelectField   | 表示选择表单元素                          |
| 7    | TextAreaField | 表示<testarea> html表单元素               |
| 8    | PasswordField | 表示<input type ='password'> HTML表单元素 |
| 9    | SubmitField   | 表示<input type ='submit'>表单元素        |

例如，可以设计一个包含文本字段的表单，如下所示 -

```python
from flask_wtf import Form
from wtforms import TextField

class ContactForm(Form):
    name = TextField("Name Of Student")
```

除了`name`字段之外，还会自动创建一个CSRF令牌的隐藏字段。 这是为了防止跨站请求伪造攻击。

渲染时，这将产生一个等效的HTML脚本，如下所示。

```python
<input id = "csrf_token" name = "csrf_token" type = "hidden" />
<label for = "name">Name Of Student</label><br>
<input id = "name" name = "name" type = "text" value = "" />
```

用户定义的表单类在Flask应用程序中使用，表单使用模板呈现。

```python
from flask import Flask, render_template
from forms import ContactForm
app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/contact')
def contact():
    form = ContactForm()
    return render_template('contact.html', form = form)

if __name__ == '__main__':
    app.run(debug = True)
```

WTForms包也包含验证器类，在验证表单域时非常有用。 以下列表显示了常用的验证器。

| 编号 | 验证器类     | 描述                                       |
| ---- | ------------ | ------------------------------------------ |
| 1    | DataRequired | 检查输入栏是否为空                         |
| 2    | Email        | 检查字段中的文本是否遵循电子邮件ID约定     |
| 3    | IPAddress    | 验证输入字段中的IP地址                     |
| 4    | Length       | 验证输入字段中字符串的长度是否在给定范围内 |
| 5    | NumberRange  | 在给定范围内的输入字段中验证一个数字       |
| 6    | URL          | 验证输入字段中输入的URL                    |

将联系表单的`name`字段应用`'DataRequired'`验证规则。

```python
name = TextField("Name Of Student",[validators.Required("Please enter your name.")])
```

表单对象的`validate()`函数验证表单数据，并在验证失败时抛出验证错误。 错误消息被发送到模板。 在HTML模板中，错误消息是动态呈现的。

```python
{% for message in form.name.errors %}
   {{ message }}
{% endfor %}
```

以下示例演示了上面给出的概念。联系人表单代码如下(*forms.py*)。

```python
from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField

from wtforms import validators, ValidationError

class ContactForm(Form):
    name = TextField("学生姓名",[validators.Required("Please enter your name.")])
    Gender = RadioField('性别', choices = [('M','Male'),('F','Female')])
    Address = TextAreaField("地址")

    email = TextField("Email",[validators.Required("Please enter your email address."),
      validators.Email("Please enter your email address.")])

    Age = IntegerField("年龄")
    language = SelectField('语言', choices = [('cpp', 'C++'), ('py', 'Python')])
    submit = SubmitField("提交")
```

验证器应用于名称和电子邮件字段。下面给出的是Flask应用程序脚本(*formexample.py*)。

```python
from flask import Flask, render_template, request, flash
from forms import ContactForm
app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
       if form.validate() == False:
          flash('All fields are required.')
          return render_template('contact.html', form = form)
       else:
          return render_template('success.html')
    elif request.method == 'GET':
          return render_template('contact.html', form = form)

if __name__ == '__main__':
    app.run(debug = True)
```

模板的脚本(*contact.html*)如下所示 -

```python
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Flask示例</title>
</head>
   <body>

     <h2 style = "text-align: center;">联系人表单</h2>

      {% for message in form.name.errors %}
         <div>{{ message }}</div>
      {% endfor %}

      {% for message in form.email.errors %}
         <div>{{ message }}</div>
      {% endfor %}

      <form action = "http://localhost:5000/contact" method = post>
         <fieldset>
            <legend>填写项</legend>
            {{ form.hidden_tag() }}

            <div style = font-size:20px; font-weight:bold; margin-left:150px;>
               {{ form.name.label }}<br>
               {{ form.name }}
               <br>

               {{ form.Gender.label }} {{ form.Gender }}
               {{ form.Address.label }}<br>
               {{ form.Address }}
               <br>

               {{ form.email.label }}<br>
               {{ form.email }}
               <br>

               {{ form.Age.label }}<br>
               {{ form.Age }}
               <br>

               {{ form.language.label }}<br>
               {{ form.language }}
               <br>
               {{ form.submit }}
            </div>

         </fieldset>
      </form>

   </body>
</html>
```

在Python shell中运行*formexample.py*，并访问URL => `http://localhost:5000/contact` 。 联系人表单将显示如下。