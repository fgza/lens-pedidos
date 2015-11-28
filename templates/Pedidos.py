import sqlite3

conn = sqlite3.connect('compras.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE pedidos(Pedido VARCHAR, Proveedor VARCHAR, Fecha DATE, Importe REAL)")

def add_data():
    c.execute("INSERT INTO pedidos VALUES('1','Philips','1/29/2015','10000.45')")
    conn.commit()

def add_data_dynamic():
    pedi = "2"
    prov = 'Osram'
    fecha = '1/29/2015'
    monto = 10000.45
    c.execute("INSERT INTO pedidos (Pedido, Proveedor, Fecha, Importe) VALUES( ?,?,?,?)", (pedi,prov,fecha,monto))
    conn.commit()

def update_proveedor():
    sql = "UPDATE pedidos SET Proveedor = ? WHERE proveedor == ?"
    #sql = "UPDATE pedidos SET Proveedora = 'Phillips'"
    provant = "Osram"
    provnuevo = 'OSRAM'
    c.execute(sql, [(provnuevo),(provant)])
    conn.commit()

def update_fecha():
    sql = "UPDATE pedidos SET Fecha = ? WHERE Fecha == ?"
    #sql = "UPDATE pedidos SET Proveedora = 'Phillips'"
    provant = "Osram"
    provnuevo = 'OSRAM'
    c.execute(sql, [(provnuevo),(provant)])
    conn.commit()

def delete_provedor():
    sql = "DELETE FROM pedidos WHERE Proveedor == ?"
    prov = 'OSRAM'
    c.execute(sql, [(prov)])
    conn.commit()

def read_data():    
    sql = "SELECT * FROM pedidos" # WHERE Proveedor == ? AND Pedido == ?"
    #pedi = "2"
    #prov = 'Osram'
    for row in c.execute(sql): #, [(prov),(pedi)]):
        print(row)

#create_table()
add_data()
add_data_dynamic()
#update_proveedor()
#delete_provedor()
read_data()

conn.close
