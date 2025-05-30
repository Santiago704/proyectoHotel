import mysql.connector  # Corregí el import, es mejor usar directamente `mysql.connector`
import csv
import os

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

    def export_all_tables_to_csv(self, output_dir="csv_exports"):
        if not self._connection:
            print("❌ No hay conexión establecida.")
            return

        try:
            cursor = self._connection.cursor()
            cursor.execute("SHOW TABLES")
            tablas = [tabla[0] for tabla in cursor.fetchall()]
            cursor.close()

            for tabla in tablas:
                self.export_table_to_csv(tabla, output_dir)

            print("📦 Exportación completa de todas las tablas.")
        except mysql.connector.Error as err:
            print("❌ Error al obtener lista de tablas:", err)

            def export_table_to_csv(self, table_name, output_dir="csv_exports"):
                if not self._connection:
                    print("❌ No hay conexión establecida.")
                    return

                os.makedirs(output_dir, exist_ok=True)
                ruta_salida = os.path.join(output_dir, f"{table_name}.csv")

                try:
                    cursor = self._connection.cursor()
                    cursor.execute(f"SELECT * FROM {table_name}")
                    rows = cursor.fetchall()
                    column_names = [i[0] for i in cursor.description]

                    with open(ruta_salida, "w", newline="", encoding="utf-8") as f:
                        writer = csv.writer(f)
                        writer.writerow(column_names)
                        writer.writerows(rows)

                    print(f"✅ Tabla '{table_name}' exportada a: {ruta_salida}")
                except mysql.connector.Error as err:
                    print(f"❌ Error al exportar tabla '{table_name}': {err}")
                finally:
                      cursor.close()