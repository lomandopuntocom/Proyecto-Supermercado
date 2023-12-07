from tkinter import messagebox
from model.conexion_db import ConexionDB

class CategoriaDB:
    def __init__(self, nombre, descripcion):  # Corrected the constructor method name
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
    def __init__(self, nombre, descripcion, precio, id_categoria, id_proveedor):  # Corrected the constructor method name
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio 

def agregar_producto(product):
    conexion = ConexionDB()
    sql = '''INSERT INTO producto ("id", nombre, descripcion, precio)
         VALUES (producto_sec.NEXTVAL, :nombre, :descripcion, :precio)'''
    try:
        conexion.cursor.execute(sql, {'nombre': categoria.nombre, 'descripcion': categoria.descripcion, 'precio':categoria.precio})
    except Exception as e:
        titulo = 'Conexion a la base de datos'
        mensaje = 'No se pudo agregar el producto: ' + str(e)
        messagebox.showerror(titulo, mensaje)
    finally:
        if conexion:
            conexion.cerrar()