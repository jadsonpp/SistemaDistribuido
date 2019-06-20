import pika
import sys
import time
from random import uniform
# Gera dados aleatoriamente.
def geraTemperatura():
    return str(uniform(10,40))
#Gera a humidade aleatoriamente.
def geraHumidade():
    return str(uniform(40,90))
#Porcentagem.
def geraPressao():
    return str(uniform(0,1))

def mandaMSG(msg:str):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    message = ' '.join(sys.argv[1:]) or msg
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))
    print(" [x] Sent %r" % message)
    connection.close()

while(True):
    msg = geraTemperatura()
    mandaMSG(msg)
    time.sleep(10)
    msg = geraHumidade()
    mandaMSG(msg)
    time.sleep(10)
    msg = geraPressao()
    mandaMSG(msg)
    time.sleep(10)
