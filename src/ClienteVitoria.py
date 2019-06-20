import pika
import sys
import time
import random
import json

# Gera dados aleatoriamente.
def geraNumero(min,max):
    num = str(random.randrange(min, max)) + "." + str(random.randrange(0, 99))
    return num

def geraTemperatura():
    return geraNumero(10,40)
#Gera a humidade aleatoriamente.
def geraUmidade():
    return geraNumero(40,90)
#Porcentagem.
def geraPressao():
    return geraNumero(0,1)

#cria um JSON com os dados.
def criaDados(localizacao):
    dic = {}
    dic['Temperatura']= geraTemperatura()
    dic['Umidade'] = geraUmidade()
    dic['Pressao'] = geraPressao()
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
    msg = criaDados("Vitoria")
    mandaMSG(msg)
    time.sleep(30)



'''
    -Não ta atualizando a localização-
def main(args):
    print(args)
    if(len(args) != 2):
        print("Entre com a localização.")
    else:

        while (True):
            msg = criaDados(args[1])
            mandaMSG(msg)
            time.sleep(10)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

'''