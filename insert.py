import sys, os
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db= 'test', charset='utf8')
cursor = conn.cursor()

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
