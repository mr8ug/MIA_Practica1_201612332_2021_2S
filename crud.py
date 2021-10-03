
from flask import Flask, jsonify, render_template
from flask_cors import CORS
import psycopg2



app = Flask(__name__, template_folder='templates')


# IMPLEMENTAR CORS PARA NO TENER ERRORES AL TRATAR ACCEDER AL SERVIDOR DESDE OTRO SERVER EN DIFERENTE LOCACIÓN
CORS(app)

DB_HOST = "localhost"
DB_NAME = "practica1"
DB_USER = "postgres"
DB_PASS = "campos31"


try:
    con = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST)

    cur = con.cursor()
    print(con.status)

#REALIZA LA CONSULTA Y RETORNA EL JSON
    def consultar(script_name):
        try:
            with open("consultas/"+str(script_name)+".sql",encoding='utf-8') as f:
                cur.execute(f.read())
                rows = cur.fetchall()
                resultados = jsonify(rows)                
                
                return resultados
                #return render_template('resultado.html',resultado=resultados)
        except Exception as err:
            return "<h1>Error: {0} </h1>".format(err)

#PAGINA INICIAL
    @app.route("/")
    def home():
        return render_template('home.html')

#ENDPOINTS PARA CADA CONSULTA
    @app.route('/consulta1', methods=['GET'])
    def consulta1():
        return consultar("consulta1")

    @app.route('/loadcsv', methods=['GET'])
    def loadcsv():
        return consultar("loadcsv")

    #movera de la tabla temporal a el respectivo modelo
    @app.route('/loadData', methods=['GET'])
    def loadData():
        consultar("loadcsv")
        return consultar("modelo")


    
#ARRANQUE DE APLICACION
    if __name__ == "__main__":
        app.run(host='0.0.0.0')

    
#MOSTRAR EL ERROR 
except Exception as err:
    print('Error: {0} >'.format(err))
