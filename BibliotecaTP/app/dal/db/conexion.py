import sqlite3

class ConexionBD:
    _instancia = None

    def __init__(self, archivo="biblioteca.db"): # para que sea en memoria reemplazar "biblioteca.db" por ":memory:"
        self.conn = sqlite3.connect(archivo)
        self.conn.row_factory = sqlite3.Row
        self.crear_tablas()

    @classmethod
    def get_instancia(cls):
        if cls._instancia is None:
            cls._instancia = ConexionBD()
        return cls._instancia

    def crear_tablas(self):
        cur = self.conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            autor TEXT,
            disponible INTEGER DEFAULT 1
        )""")
        cur.execute("""CREATE TABLE IF NOT EXISTS socios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            email TEXT
        )""")
        cur.execute("""CREATE TABLE IF NOT EXISTS prestamos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_socio INTEGER,
            id_libro INTEGER,
            fecha_prestamo TEXT,
            fecha_devolucion TEXT,
            devuelto INTEGER DEFAULT 0
        )""")
        self.conn.commit()
