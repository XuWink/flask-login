from functools import wraps
from flask import abort
from flask_login import current_user

'''创建一个自定义装饰器来检查用户的权限'''
def role_required(role):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            current_role = None
            if current_user.role == '0':
                current_role = 'admin'
            else:
                current_role = 'user'
            if not current_user.role == role:
                abort(403)  # 403 Forbidden
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper