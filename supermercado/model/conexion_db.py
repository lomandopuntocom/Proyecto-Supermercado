import oracledb

class ConexionDB:
    def __init__(self):
        self.conexion = oracledb.connect(user='SYSTEM', password='123456789', dsn='localhost:1521/orcl')
        self.cursor = self.conexion.cursor()

    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()
