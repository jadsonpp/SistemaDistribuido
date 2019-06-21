import pika
import sys
import time
import random
import json


def geraTemperatura():
    return str(random.randint(20,40))


#cria um JSON com os dados.
def criaDados(localizacao):
    dic = {}
    dic['Temperatura']= geraTemperatura()
    dic['Localizacao'] = localizacao
    msg = json.dumps(dic)
    return msg

#Faz o channel e manda a msg.
def mandaMSG(msg:json):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    message = ' '.join(sys.argv[1:]) or (msg)
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))

    connection.close()

#Teste.

while (True):
    msg = criaDados("Fundao")
    mandaMSG(msg)
    time.sleep(30)



