from conexion_db import ConexionDB
def crear_tabla():
    conexion = ConexionDB()
    sql = '''insert into persona values (2, 'Jun', 'Juan@gmail.cm', 9123522, 'EriqueSegoviano')'''
    conexion.cursor.execute(sql)
    conexion.cerrar()

crear_tabla()