import pika
import sys
from random import uniform
# Gera dados aleatoriamente.
def geraTemperatura():
    return uniform(10,40)
#Gera a humidade aleatoriamente.
def geraHumidade():
    return uniform(40,90)
#Porcentagem.
def geraPressao():
    return uniform(0,1)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or str(geraTemperatura())
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent
    ))
print(" [x] Sent %r" % message)
connection.close()