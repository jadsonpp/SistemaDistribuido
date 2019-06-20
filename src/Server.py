import pika
import time
import psycopg2
import json

#info bd -> Elephant SQL
DB_NAME = "uivesmor"
DB_HOST = "tuffi.db.elephantsql.com"
DB_USER = "uivesmor"
DB_PASSWORD = "pG0a8znwEl-tU2DvG5WP-tAyE7VH5Zkr"
DB_PORT = "5432"

#Conecta ao Banco.
try:
    conn = psycopg2.connect(database=DB_NAME,
                        user=DB_USER,
                        password=DB_PASSWORD,
                        host=DB_HOST,
                        port=DB_PORT)
    print("Conectado.")
except:
    print("database não encontrado.")

#Conecatar a fila.
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    cur = conn.cursor()
    msg = json.loads(body)
    cur.execute("INSERT INTO sensores (umidade, temperatura, pressao, localizacao) "
                "values ("+ "'"+msg['Umidade']+"','" +msg['Temperatura']+"','"+
                msg['Pressao']+"','"+msg['Localizacao']+"');")

    conn.commit()
    ch.basic_ack(delivery_tag=method.delivery_tag)
    time.sleep(body.count(b'.'))
    #conn.close()


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)
channel.start_consuming()



'''
ClienteSerra.py

insert into sensores(umidade, temperatura, pressao, localizacao) values ('0.4','33.4','34.4','vila velha');


'''