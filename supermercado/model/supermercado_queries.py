from tkinter import messagebox
from model.conexion_db import ConexionDB

class CategoriaDB:
    def __init__(self, nombre, descripcion): 
        self.nombre = nombre
        self.descripcion = descripcion

def agregar_cat(categoria):
    conexion = ConexionDB()
    sql = '''INSERT INTO categoria ("id", nombre, descripcion)
         VALUES (categoria_sec.NEXTVAL, :nombre, :descripcion)'''
    try:
        conexion.cursor.execute(sql, {'nombre': categoria.nombre, 'descripcion': categoria.descripcion})
    except Exception as e:
        titulo = 'Conexion a la base de datos'
        mensaje = 'No se pudo agregar la categoría: ' + str(e)
        messagebox.showerror(titulo, mensaje)
    finally:
        if conexion:
            conexion.cerrar()



class ProductoDB:
    def __init__(self, nombre, descripcion, precio, id_categoria, id_proveedor, stock, fecha_ingreso):  
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio 
        self.id_categoria=id_categoria
        self.id_proveedor=id_proveedor
        self.stock=stock
        self.fecha_ingreso=fecha_ingreso

def agregar_producto(producto):
    conexion = ConexionDB()
    sql = '''INSERT INTO producto ("id", nombre, descripcion, precio, id_categoria, id_proveedor)
         VALUES (producto_sec.NEXTVAL, :nombre, :descripcion, :precio,:id_categoria, :id_proveedor)'''
    try:
        conexion.cursor.execute(sql, {'nombre': producto.nombre, 'descripcion': producto.descripcion, 'precio':producto.precio, 'id_categoria':producto.id_categoria, 'id_proveedor':producto.id_proveedor})
        conexion.conexion.commit()  
        sql_get_last_id = 'SELECT producto_sec.CURRVAL FROM dual'
        conexion.cursor.execute(sql_get_last_id)
        id_producto = conexion.cursor.fetchone()[0]
        agregar_inventario(id_producto, conexion, producto.stock, producto.fecha_ingreso)
    except Exception as e:
        titulo = 'Conexion a la base de datos'
        mensaje = 'No se pudo agregar el producto: ' + str(e)
        messagebox.showerror(titulo, mensaje)
    finally:
        if conexion:
            conexion.cerrar()



def agregar_inventario(id_producto, conexion, stock, fecha_ingreso):
    sql ='''INSERT INTO inventario ("id", stock, fecha_ingreso, id_producto)
            VALUES (inventario_sec.NEXTVAL, :stock, :fecha_ingreso,:id_producto)'''    
    try:
        conexion.cursor.execute(sql, {'stock':stock, 'fecha_ingreso': fecha_ingreso, 'id_producto': id_producto})
        conexion.conexion.commit() 

    except Exception as e:
        titulo = 'Conexion a la base de datos'
        mensaje = 'No se pudo agregar el proveedor: ' + str(e)
        messagebox.showerror(titulo, mensaje)
class PersonaDB:
    def __init__(self, nombre, email, contacto, direccion):  
        self.nombre = nombre
        self.email = email
        self.contacto = contacto
        self.direccion=direccion

def agregar_persona(persona):
    conexion = ConexionDB()
    sql = '''INSERT INTO persona ("id", nombre, email, num_contacto, direccion)
         VALUES (persona_sec.NEXTVAL, :nombre, :email, :num_contacto, :direccion)'''
    try:
        conexion.cursor.execute(sql, {'nombre': persona.nombre, 'email': persona.email, 'num_contacto':persona.contacto, 'direccion':persona.direccion})
        conexion.conexion.commit()  
        sql_get_last_id = 'SELECT persona_sec.CURRVAL FROM dual'
        conexion.cursor.execute(sql_get_last_id)
        id_persona = conexion.cursor.fetchone()[0]
        agregar_proveedor(id_persona, conexion)
    except Exception as e:
        titulo = 'Conexion a la base de datos'
        mensaje = 'No se pudo agregar a la persona: ' + str(e)
        messagebox.showerror(titulo, mensaje)
    finally:
        if conexion:
            conexion.cerrar()

def agregar_proveedor(id_persona, conexion):
    sql_proveedor = '''
        INSERT INTO proveedor ("id", id_persona)
        VALUES (proveedor_sec.NEXTVAL, :id_persona)
    '''
    try:
        conexion.cursor.execute(sql_proveedor, {'id_persona': id_persona})
        conexion.conexion.commit() 

    except Exception as e:
        titulo = 'Conexion a la base de datos'
        mensaje = 'No se pudo agregar el proveedor: ' + str(e)
        messagebox.showerror(titulo, mensaje)

