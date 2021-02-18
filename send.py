import sys
import pika
import hashlib

m = hashlib.md5() 

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

try:
    b_msg = sys.argv[1]
except:
    b_msg = "Hello World!"

m.update(b_msg.encode("utf-8"))
sha_val = m.hexdigest()
#print(sha_val)

channel.basic_publish(exchange='',routing_key='hello',body=sha_val)
print(f" [x] Sent {sha_val}")
connection.close()
