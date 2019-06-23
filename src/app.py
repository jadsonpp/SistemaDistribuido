from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

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




colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]




@app.route('/')
def lineFundao():
    cur = conn.cursor()
    lstDataHora = []  # LABEL
    lstValues = []  # VALORES
    cur.execute("SELECT dataHora,temperatura from sensores where localizacao = 'Fundao'")
    for row in cur:
        dataHora = row[0].strftime('%d/%m/%Y %H:%M:%S')
        lstDataHora.append(dataHora)
        lstValues.append(row[1])

    line_labels=lstDataHora
    line_values=lstValues
<<<<<<< HEAD
    return render_template('relatorio.html', title='Temperatura Fundao', max=50, labels=line_labels, values=line_values)
=======
    return render_template('line_chart.html', title='Temperatura', max=50, labels=line_labels, values=line_values)
>>>>>>> 58fd2ea4d90c399523b267d73c791a0e03ed34a6

@app.route('/Serra')
def lineSerra():
    cur = conn.cursor()
    lstDataHora = []  # LABEL
    lstValues = []  # VALORES
    cur.execute("SELECT dataHora,temperatura from sensores where localizacao = 'Serra'")

    for row in cur:
        dataHora = row[0].strftime('%d/%m/%Y %H:%M:%S')
        lstDataHora.append(dataHora)
        lstValues.append(row[1])

    line_labels=lstDataHora
    line_values=lstValues
<<<<<<< HEAD
    return render_template('relatorio.html', title='Temperatura Serra', max=50, labels=line_labels, values=line_values)
=======
    return render_template('line_chart.html', title='Temperatura', max=50, labels=line_labels, values=line_values)
>>>>>>> 58fd2ea4d90c399523b267d73c791a0e03ed34a6



@app.route('/Vitoria')
def lineVitoria():
    cur = conn.cursor()
    lstDataHora = []  # LABEL
    lstValues = []  # VALORES
    cur.execute("SELECT dataHora,temperatura from sensores where localizacao = 'Vitoria'")

    for row in cur:
        dataHora = row[0].strftime('%d/%m/%Y %H:%M:%S')
        lstDataHora.append(dataHora)
        lstValues.append(row[1])

    line_labels=lstDataHora
    line_values=lstValues
<<<<<<< HEAD
    return render_template('relatorio.html', title='Temperatura Vitória', max=50, labels=line_labels, values=line_values)
=======
    return render_template('line_chart.html', title='Temperatura', max=50, labels=line_labels, values=line_values)
>>>>>>> 58fd2ea4d90c399523b267d73c791a0e03ed34a6


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)