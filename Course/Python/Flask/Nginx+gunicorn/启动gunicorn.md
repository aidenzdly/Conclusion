1. (venv) $ pip install gunicorn

2. 创建sh执行文件启动gunicorn（方法很多种，conf、py等启动方式）

   ```python
   export FLASK_APP=app
   nohup gunicorn -b 127.0.0.1:9999 app:app > /dev/null 2>&1 &
   #gunicorn -b 127.0.0.1:9999 app:app &
   
   ```

   

