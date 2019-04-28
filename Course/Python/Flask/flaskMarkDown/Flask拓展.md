## Flask拓展

Flask通常被称为微框架，因为核心功能包括基于Werkzeug的WSGI和路由以及基于Jinja2的模板引擎。 此外，Flask框架还支持cookie和会话以及Web助手，如JSON，静态文件等。显然，这对于开发完整的Web应用程序来说还不够。 这是为什么还要Flask扩展插件。 Flask扩展为Flask框架提供了可扩展性。

Flask有大量的扩展可用。 Flask扩展是一个Python模块，它为Flask应用程序添加了特定类型的支持。 Flask扩展注册表是一个可用扩展的目录。 所需的扩展名可以通过pip实用程序下载。

在本教程中，我们将讨论以下重要的Flask扩展 -

- **Flask Mail** − 为Flask应用程序提供SMTP接口

- **Flask WTF** − 添加了WTForms的渲染和验证

- **Flask SQLAlchemy** − 将SQLAlchemy支持添加到Flask应用程序中

- **Flask Sijax** − Sijax接口 - 使AJAX易于在Web应用程序中使用Python/jQuery库

每种类型的扩展通常提供有关其使用情况的大量文档。 由于扩展是一个Python模块，因此需要导入才能使用它。 Flask扩展名通常命名为`flask-foo`。导入语法如下，

```python
from flask_foo import [class, function]
```

对于低于`0.7`的Flask版本，还可以使用语法 -

```python
from flask.ext import foo
```

为此，需要激活兼容性模块。 它可以通过运行`flaskext_compat.py`来安装 -

```python
import flaskext_compat
flaskext_compat.activate()
from flask.ext import foo
```

