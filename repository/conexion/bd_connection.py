import mysql.connector  # Corregí el import, es mejor usar directamente `mysql.connector`

class Conexion:

    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self._connection = None

    def connection(self):
        try:
            self._connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexión Establecida")
        except mysql.connector.Error as err:
            print("Error al conectar a la base de datos:", err)

    def disconnect(self):
        if self._connection:
            self._connection.close()
            print("Conexión Cerrada")

    def execute_query(self, query, params=None):
        if not self._connection:
            print("No hay conexión establecida.")
            return None
        cursor = self._connection.cursor(buffered=True)
        try:
            cursor.execute(query, params)
            self._connection.commit()
            print("Registro guardado exitosamente")
            if query.lower().startswith('select'):
                result = cursor.fetchall()
                return result
        except mysql.connector.Error as err:
            print("Error al ejecutar la consulta:", err)
            return None
        finally:
            cursor.close()


    def fetch_one(self, query, params):
        if not self._connection:
            print("No hay conexión establecida")
            return None
        cursor = self._connection.cursor(dictionary=True)
        cursor.execute(query, params)
        result = cursor.fetchone()
        cursor.close()
        return result