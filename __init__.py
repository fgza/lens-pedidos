from flask import Flask, render_template
#from flaskext.mysql import MySQL
#from flask.ext.sqlalchemy import SQLAlchemy
import os
from dbconnect import connection

app = Flask(__name__)

@app.route('/')
def homepage():
    try:
        return render_template('index.html')
    except Exception as e:
        return(str(e))
    
@app.route('/about/')
def aboutpage():
    try:
        body_text = "Aplicaccion de Pedidos de Lens Lighting. Desarrollada por Fidel Garza En Python, con Flask Framework, con Bootstrap y con ayuda de Udemy Python Web Programming [2015]"
        return render_template('about.html', body_text = body_text)
    except Exception as e:
        return(str(e))

@app.route('/proveedores/')
def proveedorespage():
    try:
        c, conn = connection()
        c.execute("SELECT NOMBRE, RFC, TELEFONOS, DIRECCION, CIUDAD FROM proveedores");
        data = c.fetchone()
        name = "Base de Datos"
        lista_provedores = data[1]
        return lista_provedores
        #return render_template('proveedores.html', name = name,
        #                       lista_proveedores = lista_provedores)
    except Exception as e:
        return(str(e))

@app.errorhandler(404)
def four_oh_four(e):
    body_text = "No encontrada"
    return render_template('about.html', body_text = body_text)

    
if __name__ == "__main__":
    #app.debug = True
    #app.secret_key = 'SuperSecretKey'
    
    #SQL-Alchemy
    #basedir = os.path.abspath(os.path.dirname(__file__))
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:figach5t@localhost/Lens'
    #app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    #db = SQLAlchemy(app)


    #mysql de flaskext.mysql
    #mysql = MySQL()
    #app.config['MYSQL_DATABASE_USER'] = 'root'
    #app.config['MYSQL_DATABASE_PASSWORD'] = 'figach5t'
    #app.config['MYSQL_DATABASE_DB'] = 'Lens'
    #app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    #mysql.init_app(app)
    
    app.run()
