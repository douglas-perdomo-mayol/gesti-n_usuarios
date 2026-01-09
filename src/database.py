import sqlite3 

class DataBase:
    def __init__(self, nombre_db='usuario.db'):
        self.nombre_db = nombre_db
        self._crear_tabla()

    def _conectar(self):
        return sqlite3.connect(self.nombre_db)

    def _crear_tabla(self):
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                           CREATE TABLE IF NOT EXISTS usuarios(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           nombre TEXT NOT NULL,
                           edad INTEGER NOT NULL,
                           tipo TEXT NOT NULL
                )
            ''')
            conn.commit()

    def insertar_usuario(self, nombre, edad, tipo):
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO usuarios (nombre, edad, tipo) VALUES (?, ?, ?)',
                (nombre, edad, tipo)

            )
            conn.commit()

    def obtener_mayores(self):
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT nombre, edad, tipo FROM usuarios WHERE edad >= 21'
            )
            return cursor.fetchall()