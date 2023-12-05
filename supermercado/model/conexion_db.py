import oracledb

class ConexionDB:
    def init(self):
        self.conexion = oracledb.connect(user = 'system',
            password = 'Mondongo123',
            dsn = 'localhost:1521/xe')
        self.cursor = self.conexion.cursor()

    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()