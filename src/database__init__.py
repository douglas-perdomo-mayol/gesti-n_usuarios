import sqlite3

class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect(":memory:")
        self._crear_tabla()

    def _crear_tabla(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                edad INTEGER,
                tipo TEXT
            )
        """)
        self.conn.commit()

    def insertar_usuario(self, nombre, edad, tipo):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nombre, edad, tipo) VALUES (?, ?, ?)",
            (nombre, edad, tipo)
        )
        self.conn.commit()

    def obtener_mayores(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT nombre, edad, tipo FROM usuarios WHERE edad >= 21"
        )
        return cursor.fetchall()

    def actualizar_usuario(self, nombre, nuevo_nombre, nueva_edad):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE usuarios SET nombre = ?, edad = ? WHERE nombre = ?",
            (nuevo_nombre, nueva_edad, nombre)
        )
        if cursor.rowcount == 0:
            raise ValueError("Usuario no encontrado")
        self.conn.commit()


    def eliminar_usuario(self, nombre):
        cursor = self.conn.cursor()
        cursor.execute(
            "DELETE FROM usuarios WHERE nombre = ?",
            (nombre,)
        )
        self.conn.commit()