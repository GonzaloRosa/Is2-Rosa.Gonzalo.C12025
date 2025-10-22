class LibrosDAL:
    def __init__(self, conn):
        self.conn = conn

    def agregar(self, titulo, autor):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO libros(titulo, autor) VALUES (?,?)", (titulo, autor))
        self.conn.commit()
        return cur.lastrowid

    def listar_disponibles(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM libros WHERE disponible=1")
        return cur.fetchall()

    def listar_todos(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM libros")
        return cur.fetchall()

    def cambiar_disponible(self, id_libro, disp):
        cur = self.conn.cursor()
        cur.execute("UPDATE libros SET disponible=? WHERE id=?", (disp, id_libro))
        self.conn.commit()

    def obtener(self, id_libro):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM libros WHERE id=?", (id_libro,))
        return cur.fetchone()
