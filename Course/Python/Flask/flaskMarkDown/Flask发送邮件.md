## Flask发送邮件

基于Web的应用程序通常需要具有向用户/客户端发送邮件的功能。 Flask-Mail扩展使得用任何电子邮件服务器设置一个简单接口变得非常简单。

起初，Flask-Mail扩展可使用pip工具来安装，如下所示 -

```python
pip install Flask-Mail
```

然后需要通过设置以下应用程序参数的值来配置Flask-Mail。

| 编号 | 参数                   | 描述                                        |
| ---- | ---------------------- | ------------------------------------------- |
| 1    | MAIL_SERVER            | 邮件服务器的名称/IP地址                     |
| 2    | MAIL_PORT              | 所用服务器的端口号                          |
| 3    | MAIL_USE_TLS           | 启用/禁用传输安全层加密                     |
| 4    | MAIL_USE_SSL           | 启用/禁用安全套接字层加密                   |
| 5    | MAIL_DEBUG             | 调试支持，默认是Flask应用程序的调试状态     |
| 6    | MAIL_USERNAME          | 发件人的用户名                              |
| 7    | MAIL_PASSWORD          | 发件人的密码                                |
| 8    | MAIL_DEFAULT_SENDER    | 设置默认发件人                              |
| 9    | MAIL_MAX_EMAILS        | 设置要发送的最大邮件                        |
| 10   | MAIL_SUPPRESS_SEND     | 如果app.testing设置为true，则发送被抑制     |
| 11   | MAIL_ASCII_ATTACHMENTS | 如果设置为true，则将附加的文件名转换为ASCII |

`flask-mail`模块包含以下重要类的定义。



#### Mail类

它管理电子邮件消息的要求。 类构造函数采用以下形式 -

| 编号 | 方法           | 描述                    |
| ---- | -------------- | ----------------------- |
| 1    | send()         | 发送Message类对象的内容 |
| 2    | connect()      | 与邮件主机打开连接      |
| 3    | send_message() | 发送消息对象            |



#### Message类

它封装了一封电子邮件，Message类的构造函数有几个参数 -

```python
flask-mail.Message(subject, recipients, body, html, sender, cc, bcc, 
   reply-to, date, charset, extra_headers, mail_options, rcpt_options)
```

#### Message类方法

- `attach()` - 向消息添加附件。 该方法采用以下参数 -
- `filename` - 要附加的文件的名称
- `content_type` - 文件的MIME类型
- `data` - 原始文件数据
- `disposition` - 内容处置，如果有的话。

- `add_recipient()` - 向消息添加另一个收件人

在以下示例中，Google的Gmail服务的SMTP服务器用作Flask-Mail配置的MAIL_SERVER。



**第1步** - 在代码中从flask-mail模块导入Mail和Message类。

```python
from flask_mail import Mail,Message
```

**第2步** - 然后根据以下设置配置Flask-Mail。

```python
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

```

**第3步** - 创建一个Mail类的实例。

```python
mail = Mail(app)
```

**第4步** - 在由URL规则映射的Python函数(‘/‘)中设置Message对象。

```python
@app.route("/")
def index():
    msg = Message('Hello', sender = 'yourId@gmail.com', recipients = ['id1@gmail.com'])
    msg.body = "This is the email body"
    mail.send(msg)
    return "Sent"
```

**第5步** - 整个代码如下。 在Python Shell中运行以下脚本并访问URL: `http://localhost:5000/`。

```python
from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
    msg = Message('Hello', sender = 'yourId@gmail.com', recipients = ['id1@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"

if __name__ == '__main__':
    app.run(debug = True)
```

请注意，Gmail服务中的内置不安全功能可能会阻止此登录尝试，可能需要降低安全级别。 请登录到您的Gmail帐户并访问[此链接](https://www.google.com/settings/security/lesssecureapps)以降低安全性。

