from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, password, role):
        self.id = id
        self.username = username
        self.password = password
        self.role = role  # 0 管理员，1 普通用户

    def get_id(self):
        return str(self.id)