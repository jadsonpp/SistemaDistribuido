import pika,os,sys
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
    url = "amqp://jmqemkzi:1PYY-Y6M3SMIpcGSid3nGON2DVL782CR@prawn.rmq.cloudamqp.com/jmqemkzi"
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
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
    msg = criaDados("Serra")
    mandaMSG(msg)
    time.sleep(30)


