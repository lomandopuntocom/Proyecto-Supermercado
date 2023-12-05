from .conexion_db import ConexionDB

def crear_tabla():
    conexion = ConexionDB()
    sql = '''
    CREATE TABLE producto(

    )
    '''
    conexion.cursor.execute(sql)
    conexion.cerrar()

def borrar_tabla():
    