from flask import Blueprint
import pymysql
from flask import render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required
from app.config import db_config
from app.models.User import User

api = Blueprint('api_bp', __name__)

@api.route('/')
def index():
    return "Hello world!"

@api.route('/1')
@login_required
def index1():
    return "需要登录才能访问的页面"

@api.route('/2')
def index2():
    return "不需要登录就可以访问的页面"

@api.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # 数据库查询逻辑
        connection = pymysql.connect(**db_config)
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM users WHERE username = %s"
                cursor.execute(sql, (username,))
                user_data = cursor.fetchone()
                if user_data and user_data['password'] == password:  # 假设密码已经正确验证
                    user = User(user_data['id'], user_data['username'], user_data['password'], user_data['role'])
                    login_user(user, remember=True)
                    return redirect(url_for('protected'))
        finally:
            connection.close()

    return render_template('login.html')


@api.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))