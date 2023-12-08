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
    sql_insert_producto = '''
        INSERT INTO producto ("id", nombre, descripcion, precio, id_categoria, id_proveedor)
        VALUES (producto_sec.NEXTVAL, :nombre, :descripcion, :precio, :id_categoria, :id_proveedor)
    '''
    try:
        # Insertar el nuevo producto
        conexion.cursor.execute(sql_insert_producto, {
            'nombre': producto.nombre,
            'descripcion': producto.descripcion,
            'precio': producto.precio,
            'id_categoria': producto.id_categoria,
            'id_proveedor': producto.id_proveedor
        })
        conexion.conexion.commit()

        # Obtener el último ID generado
        sql_get_last_id = 'SELECT producto_sec.CURRVAL FROM dual'
        conexion.cursor.execute(sql_get_last_id)
        id_producto = conexion.cursor.fetchone()[0]

        # Agregar al inventario con el ID del producto
        agregar_inventario(id_producto, conexion, producto.stock, producto.fecha_ingreso)

    except Exception as e:
        # En caso de error, mostrar mensaje y hacer rollback
        conexion.conexion.rollback()
        titulo = 'Conexion a la base de datos'
        mensaje = 'No se pudo agregar el producto: ' + str(e)
        messagebox.showerror(titulo, mensaje)
    finally:
        # Asegurarse de cerrar la conexión
        conexion.cerrar()

def agregar_inventario(id_producto, conexion, stock, fecha_ingreso):
    sql_insert_inventario = '''
        INSERT INTO inventario ("id", stock, fecha_ingreso, id_producto)
        VALUES (inventario_sec.NEXTVAL, :stock, :fecha_ingreso, :id_producto)
    '''
    try:
        # Insertar en el inventario
        conexion.cursor.execute(sql_insert_inventario, {
            'stock': stock,
            'fecha_ingreso': fecha_ingreso,
            'id_producto': id_producto
        })
        conexion.conexion.commit()

    except Exception as e:
        # En caso de error, mostrar mensaje y hacer rollback
        conexion.conexion.rollback()
        titulo = 'Conexion a la base de datos'
        mensaje = 'No se pudo agregar al inventario: ' + str(e)
        messagebox.showerror(titulo, mensaje)


class PersonaDB:
    def __init__(self, nombre, email, contacto, direccion):  
        self.nombre = nombre
        self.email = email
        self.contacto = contacto
        self.direccion=direccion

def agregar_persona(persona):
    conexion = ConexionDB()
    sql_insert_persona = '''
        INSERT INTO persona ("id", nombre, email, num_contacto, direccion)
        VALUES (persona_sec.NEXTVAL, :nombre, :email, :num_contacto, :direccion)
    '''
    try:
        conexion.cursor.execute(sql_insert_persona, {'nombre': persona.nombre, 'email': persona.email, 'num_contacto': persona.contacto, 'direccion': persona.direccion})
        conexion.conexion.commit()

        sql_get_last_id = 'SELECT persona_sec.CURRVAL FROM dual'
        conexion.cursor.execute(sql_get_last_id)
        id_persona = conexion.cursor.fetchone()[0]

        agregar_proveedor(id_persona, conexion)

    except Exception as e:
        conexion.conexion.rollback()
        titulo = 'Conexion a la base de datos'
        mensaje = 'No se pudo agregar a la persona: ' + str(e)
        messagebox.showerror(titulo, mensaje)
    finally:
        conexion.cerrar()


def agregar_proveedor(id_persona, conexion):
    sql_insert_proveedor = '''
        INSERT INTO proveedor ("id", id_persona)
        VALUES (proveedor_sec.NEXTVAL, :id_persona)
    '''
    try:
        conexion.cursor.execute(sql_insert_proveedor, {'id_persona': id_persona})
        conexion.conexion.commit()

    except Exception as e:
        conexion.conexion.rollback()
        titulo = 'Conexion a la base de datos'
        mensaje = 'No se pudo agregar el proveedor: ' + str(e)
        messagebox.showerror(titulo, mensaje)

class VentasDB:
    def __init__(self, nombre, email, contacto, direccion, fecha, monto, metodo_pago):  
        self.nombre = nombre
        self.email = email
        self.contacto = contacto
        self.direccion = direccion
        self.fecha = fecha
        self.monto = monto
        self.metodo_pago = metodo_pago

def agregar_ventas(ventas):
    conexion = ConexionDB()
    try:
            cliente = PersonaDB(nombre_cliente, email_cliente, contacto_cliente, direccion_cliente)
            agregar_persona(cliente)

            # Registrar venta en la base de datos
            # Aquí necesitarías una función para agregar la venta
            # agregar_venta(id_cliente, id_producto, cantidad_vendida, otros detalles de la venta)

            # Actualizar inventario
            actualizar_inventario(id_producto, cantidad_vendida)

            messagebox.showinfo("Éxito", "Venta realizada y stock actualizado")

    except Exception as e:
            messagebox.showerror("Error", f"Error al realizar la venta: {e}")


def agregar_persona2(persona):
    conexion = ConexionDB()
    sql_insert_persona = '''
        INSERT INTO persona ("id", nombre, email, num_contacto, direccion)
        VALUES (persona_sec.NEXTVAL, :nombre, :email, :num_contacto, :direccion)
    '''
    try:
        conexion.cursor.execute(sql_insert_persona, {'nombre': persona.nombre, 'email': persona.email, 'num_contacto': persona.contacto, 'direccion': persona.direccion})
        conexion.conexion.commit()
        sql_get_last_id = 'SELECT persona_sec.CURRVAL FROM dual'
        conexion.cursor.execute(sql_get_last_id)
        id_persona = conexion.cursor.fetchone()[0]

        agregar_cliente(id_persona, conexion)

    except Exception as e:
        conexion.conexion.rollback()
        titulo = 'Conexion a la base de datos'
        mensaje = 'No se pudo agregar a la persona: ' + str(e)
        messagebox.showerror(titulo, mensaje)
    finally:
        conexion.cerrar()

class Nota_VentaDB:
    def __init__(self, fecha, monto, metodo_pago):  
        self.fecha = fecha
        self.monto = monto
        self.metodo_pago = metodo_pago

def agregar_nota_venta(nota_venta, id_cliente):
    conexion = ConexionDB()
    sql_insert_nota_venta = '''
        INSERT INTO nota_venta ("id", fecha, monto, metodo_pago, id_cliente)
        VALUES (nota_venta_sec.NEXTVAL, :fecha, :monto, :metodo_pago, :id_cliente)
    '''
    try:
        conexion.cursor.execute(sql_insert_nota_venta, {'fecha': nota_venta.fecha, 'monto': nota_venta.monto, 'metodo_pago': nota_venta.metodo_pago, 'id_cliente': id_cliente})
        conexion.conexion.commit()
        sql_get_last_id = 'SELECT nota_venta_sec.CURRVAL FROM dual'
        conexion.cursor.execute(sql_get_last_id)
        id_nota_venta = conexion.cursor.fetchone()[0]
        return id_nota_venta

    except Exception as e:
        conexion.conexion.rollback()
        titulo = 'Conexion a la base de datos'
        mensaje = f'No se pudo agregar la nota de venta: {e}'
        messagebox.showerror(titulo, mensaje)
        return None
    finally:
        conexion.cerrar()


class Detalle_VentaDB:
    def __init__(self, cantidad, id_producto):  
        self.cantidad = cantidad
        self.id_producto = id_producto

def agregar_detalle_venta(detalle_venta, id_nota_venta):
    conexion = ConexionDB()
    sql_insert_detalle_venta = '''
        INSERT INTO detalle_venta ("id", cantidad, id_producto, id_nota_venta)
        VALUES (detalle_venta_sec.NEXTVAL, :cantidad, :id_producto, :id_nota_venta)
    '''

    try:
        parametros = {
            'cantidad': detalle_venta.cantidad,
            'id_producto': detalle_venta.id_producto,
            'id_nota_venta': id_nota_venta
        }
        conexion.cursor.execute(sql_insert_detalle_venta, parametros)
        conexion.conexion.commit()

    except Exception as e:
        conexion.conexion.rollback()
        titulo = 'Conexion a la base de datos'
        mensaje = f'No se pudo agregar el detalle de venta: {e}'
        messagebox.showerror(titulo, mensaje)
    finally:
        conexion.cerrar()




