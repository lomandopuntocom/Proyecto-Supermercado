import oracledb
    conexion = oracledb.connect(user = 'system',
            password = 'Mondongo123',
            dsn = 'localhost:1521/xe')
        ursor = onexion.cursor()

     def cerrar(self):
        self.conexion.commit()
        self.conexion.close()