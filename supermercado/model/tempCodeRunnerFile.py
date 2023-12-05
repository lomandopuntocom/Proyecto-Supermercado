import oracledb

class ConexionDB:
    def _init_(self):
        self.base_datos = (
            user = 'SYSTEM',
            password = '123456789',
            dsn = 'localhost:1521/orcl'
        )
        self.conexion = oracledb.connect(self.base_datos)
        self.cursor = self.conexion.cursor()

    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()