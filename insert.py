import sys, os
import pymysql
import hashlib


conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db= 'test', charset='utf8')
cursor = conn.cursor()


account = str(123)
m = hashlib.md5()
m.update(account.encode("utf-8"))
password = m.hexdigest()

print(password)
os._exit(0)


for i in range(1,100000):
    print(i)
    sql = f"""
    INSERT INTO test.tmp(`val`) VALUES ({i})
    """

    try:
        cursor.execute(sql)
        conn.commit() 
    except Exception as e:
        conn.rollback()
        print(e)

os._exit(0)
