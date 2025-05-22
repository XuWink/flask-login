from app.api.login import api
from flask import render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required

from auth.auth_decorate import role_required

@login_required
@role_required('admin')
@api.route('/auth/1', methods=['GET'])
def auth_index1():
    return "这是一个需要管理员权限才能访问的页面"