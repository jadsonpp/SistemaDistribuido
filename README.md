# Trabalho de Sistemas Distribuidos 

## Especificação
O trabalho consiste em fazer um sistema distribuido capaz de monitorar as informações de um cliente (No caso a temperatura local), as informações sãos enviadas pelo cliente para um mensage broker responsável por arrumar as mensagens por fila(FIFO). 

O Mensage broker (no caso o RabbitMQ) sabe aonde encontrar o cliente e o servidor, caso o servidor esteja indisponivel, como eu usei o rabbitMQ na nuvem, as mensagens foram colocadas na fila mas só foram processadas quando o servidor estava online. 

## Tecnologias
- Linguagem de programação Python
- Microframework Flask 
- ElephantSQL (PostgreSQL hospedado na Nuvem)
- RabbitMQ 

