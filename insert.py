import sys, os
import pymysql
import random
import hashlib


conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db= 'test', charset='utf8')
cursor = conn.cursor()


#account = str(123)
#m = hashlib.md5()
#m.update(account.encode("utf-8"))
#password = m.hexdigest()
#
#print(password)
#os._exit(0)


m = hashlib.md5()
for i in range(1,100000):
    i = str(i)
    m.update(i.encode("utf-8"))
    sha_val = m.hexdigest()

    sql = f"""
    INSERT INTO test.tmp(`val`) VALUES ('{sha_val}')
    """
    print(sql)
    #continue

    try:
        cursor.execute(sql)
        conn.commit() 
    except Exception as e:
        conn.rollback()
        print(e)

    # 隨機中斷連線，模擬塞資料塞到一半斷線
    brk = random.randint(1, 100)
    if brk==5:
        conn.close()


os._exit(0)
