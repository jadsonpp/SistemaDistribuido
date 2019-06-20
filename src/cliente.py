import pika
import sys
from random import uniform
# Gera dados.
def geraTemperatura():
    return  uniform(-10,50)

def geraHumidade():
    return  uniform(300,1200)

def geraTemperatura():
    return  uniform(-10,50)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent
    ))
print(" [x] Sent %r" % message)
connection.close()