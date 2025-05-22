# flask-login

1.初始化项目

```shell
mkdir flask-login && cd flask-login
git init
git remote add origin https://github.com/XuWink/flask-login.git\
git pull origin main
```

2. 创建虚拟环境
   ```shell
   python -m venv venv
   .\venv\Scripts\activate
   pip install flask flask-login pymysql -i  https://pypi.tuna.tsinghua.edu.cn/simple
   ```
3. 代码框架
   ```shell
   D:.
   ├─app
   │  ├─api
   │  │  └─login.py
   │  ├─auth
   │  │  
   │  ├─models
   │  │  └─User.py
   │  ├─templates
   │  └─login.html
   └─venv
   ```
4. 创建蓝图，flask app由多模块组成
5. 编写代码，实现flask login
