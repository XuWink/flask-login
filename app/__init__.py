import json
from flask import Flask
import pymysql

from app.config import db_config

from app.auth import auth
from app.api.login import api

from flask_login import LoginManager
from app.models.User import User

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    # 数据库查询逻辑
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE id = %s"
            cursor.execute(sql, (user_id,))
            user_data = cursor.fetchone()
            if user_data:
                return User(user_data['id'], user_data['username'], user_data['password'], user_data['role'])
    finally:
        connection.close()
    return None

def create_app():
    app = Flask(__name__)

    app.secret_key = 'pojqwfnmapsoidfpaif'  # 必须设置一个密钥

    login_manager.init_app(app)


    # 注册蓝图
    app.register_blueprint(api)
    app.register_blueprint(auth)

    return app