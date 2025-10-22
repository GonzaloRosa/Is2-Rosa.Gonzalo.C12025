class PrestamosDAL:
    def __init__(self, conn):
        self.conn = conn

    def prestar(self, id_socio, id_libro, fecha_prestamo, fecha_devolucion):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO prestamos(id_socio,id_libro,fecha_prestamo,fecha_devolucion) VALUES (?,?,?,?)",
                    (id_socio, id_libro, fecha_prestamo, fecha_devolucion))
        self.conn.commit()
        return cur.lastrowid

    def buscar_activo(self, id_socio, id_libro):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM prestamos WHERE id_socio=? AND id_libro=? AND devuelto=0", (id_socio, id_libro))
        return cur.fetchone()

    def devolver(self, id_prestamo):
        cur = self.conn.cursor()
        cur.execute("UPDATE prestamos SET devuelto=1 WHERE id=?", (id_prestamo,))
        self.conn.commit()

    def listar_activos(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM prestamos WHERE devuelto=0")
        return cur.fetchall()
