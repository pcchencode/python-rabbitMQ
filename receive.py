import pika
import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db= 'test', charset='utf8')
cursor = conn.cursor()


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def insert_into_db(val):
    sql = f"""
    INSERT INTO test.tmp(`val`) VALUES ('{val}')
    """
    print(sql)
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)
    
    return


print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    body = body.decode("utf-8")
    insert_into_db(val=body)
    #print(f" [x] Received %r {body}")
    print(f" [x] Received {body}")

channel.basic_consume('hello',callback)

# 每跑一次 reveive.py 都會重新插一次，應該要每跑一次都把 message queue 給清空
channel.start_consuming()
