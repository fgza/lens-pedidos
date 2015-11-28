import MySQLdb

def connection():
    conn = MySQLdb.connect(host='localhost',
                           user='root',
                           passwd='figach5t',
                           db='Lens')
    c = conn.cursor()

    return c, conn

if __name__ == '__main__':
    c, conn = connection()
    print('Conectado a Base de Datos Lens')
