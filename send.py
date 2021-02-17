import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

try:
    b_msg = sys.argv[1]
except:
    b_msg = "Hello World!"


channel.basic_publish(exchange='',routing_key='hello',body=b_msg)
print(f" [x] Sent {b_msg}")
connection.close()
