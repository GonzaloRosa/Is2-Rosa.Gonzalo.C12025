class SociosDAL:
    def __init__(self, conn):
        self.conn = conn

    def agregar(self, nombre, email):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO socios(nombre,email) VALUES (?,?)", (nombre, email))
        self.conn.commit()
        return cur.lastrowid

    def listar(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM socios")
        return cur.fetchall()

    def obtener(self, id_socio):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM socios WHERE id=?", (id_socio,))
        return cur.fetchone()
