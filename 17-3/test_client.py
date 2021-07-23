import pymysql

db = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="caifu123",
    db="xd_test",
    charset="utf8mb4",
    # 返回数组
    cursorclass=pymysql.cursors.DictCursor,
)


def test_conn():
    with db.cursor() as cursor:
        sql = "show tables;"
        cursor.execute(sql)
        print(sql)
        print(cursor.fetchall())


def test_select():
    with db.cursor() as cursor:
        sql = "select * from config where dict_key=%s;"
        cursor.execute(sql, ["host"])
        print(sql)
        print(cursor.fetchall())
