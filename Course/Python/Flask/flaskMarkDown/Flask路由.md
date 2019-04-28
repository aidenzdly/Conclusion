## Flask路由

现代Web框架使用路由技术来帮助用户记住应用程序URL。 无需从主页导航即可直接访问所需页面。

Flask中的`route()`装饰器用于将URL绑定到函数。 例如 -

```python
@app.route('/hello')
def hello_world():
    return 'hello world'
```

这里，URL `/hello`规则绑定到`hello_world()`函数。 因此，如果用户访问URL : `http://localhost:5000/hello` ，就会调用`hello_world()`函数，这个函数中的执行的结果输出将在浏览器中呈现。

应用程序对象的`add_url_rule()`函数也可用于将URL与函数绑定，如上例所示，使用`route()`。

```python
def hello_world():
    return 'hello world'

app.add_url_rule('/', 'hello', hello_world)
```

