import mysql.connector

# 连接到MySql数据库
conn = mysql.connector.connect(
    host="192.168.77.100", user="root", password="123456", database="mysql"
)

# 创建一个游标对象
cursor = conn.cursor()

# 执行SQL语句
cursor.execute("""select * from mybook""")

# 获取查询结果
result = cursor.fetchall()

# 打印查询到的数据
for row in result:
    print(row)

conn.close()
