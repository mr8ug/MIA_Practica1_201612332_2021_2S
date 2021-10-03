
from flask import Flask, jsonify, request, render_template, render_template_string
from flask.templating import render_template_string
from flask_cors import CORS
import psycopg2
import os
import json


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

    @app.route("/")
    def home():
      # return "<h1 style='color:blue'>ESTAMOS EN EL LABORATORIO DE ARCHIVOS !</h1>"
        return render_template('home.html')
# obtengo todos los registros de mi tabla movies que cree en mi BD

    @app.route('/toda', methods=['GET'])
    def fetch_all_movies():
        try:
            cur.execute('SELECT * FROM movies')
            rows = cur.fetchall()
            print(rows)

            return jsonify(rows)
        except Exception as err:
            return "<h1>Error: {0} </h1>".format(err)


# obtengo todos los registros de mi tabla movies que cree en mi BD

    @app.route('/consulta1', methods=['GET'])
    def consulta1():
        try:
            with open('consultas/consulta1.sql',encoding='utf-8') as f:
                cur.execute(f.read())
                #cur.execute('SELECT * FROM movies')
                rows = cur.fetchall()
                # print(rows)
                return jsonify(rows)
        except Exception as err:
            return "<h1>Error: {0} </h1>".format(err)

    @app.route('/loadcsv', methods=['GET'])
    def loadcsv():
        try:
            with open('consultas/loadcsv.sql',encoding='utf-8') as f:
                cur.execute(f.read())
                #cur.execute('SELECT * FROM movies')
                rows = cur.fetchall()
                # print(rows)
                
                return jsonify(rows)
                #return "<h1>CONSULTA 1</H1>"
        except Exception as err:
            return "<h1>Error: {0} </h1>".format(err)

        

    if __name__ == "__main__":
        app.run(host='0.0.0.0')


except Exception as err:
    print('Error: {0} >'.format(err))
