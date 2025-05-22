import pymysql

# 数据库配置
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'xuwenke',
    'database': 'flask_demo',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}