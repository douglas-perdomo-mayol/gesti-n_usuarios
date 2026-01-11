import sqlite3 

class DataBase:
    def __init__(self, nombre_db='usuario.db'):
        self.conn = sqlite3.connect(nombre_db)
        self._crear_tabla()

    def _crear_tabla(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                edad INTEGER NOT NULL,
                tipo TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def insertar_usuario(self, nombre, edad, tipo):
        cursor = self.conn.cursor()
        cursor.execute(
            'INSERT INTO usuarios (nombre, edad, tipo) VALUES (?, ?, ?)',
            (nombre, edad, tipo) 
        )
        self.conn.commit()
        return cursor.lastrowid

    def obtener_mayores(self):
        cursor = self.conn.cursor()
        cursor.execute(
            'SELECT id, nombre, edad, tipo FROM usuarios WHERE edad >= 21'
        )
        return cursor.fetchall()

    def actualizar_usuario(self, nombre, nuevo_nombre, nueva_edad):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE usuarios SET nombre = ?, edad = ? WHERE nombre = ?",
            (nuevo_nombre, nueva_edad, nombre)
        )
        self.conn.commit()
        return cursor.rowcount > 0


    def eliminar_usuario(self, nombre):
        cursor = self.conn.cursor()
        cursor.execute(
            'DELETE FROM usuarios WHERE nombre = ?',
            (nombre,)
        )
        self.conn.commit()
        return cursor.rowcount > 0