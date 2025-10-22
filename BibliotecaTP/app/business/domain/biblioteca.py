class Biblioteca:
    def __init__(self, libros, socios, prestamos):
        self.libros = libros
        self.socios = socios
        self.prestamos = prestamos

    def agregar_socio(self, nombre, email):
        return self.socios.agregar(nombre, email)

    def agregar_libro(self, titulo, autor):
        return self.libros.agregar(titulo, autor)

    def prestar_libro(self, id_socio, id_libro):
        socio = self.socios.obtener(id_socio)
        if not socio:
            raise ValueError("Socio no existe")
        libro = self.libros.obtener(id_libro)
        if not libro or libro["disponible"] == 0:
            raise ValueError("Libro no disponible")
        from datetime import datetime, timedelta
        fecha_prestamo = datetime.now()
        fecha_devolucion = fecha_prestamo + timedelta(days=14)
        id_prestamo = self.prestamos.prestar(id_socio, id_libro, fecha_prestamo.isoformat(), fecha_devolucion.isoformat())
        self.libros.cambiar_disponible(id_libro, 0)
        return id_prestamo

    def devolver_libro(self, id_socio, id_libro):
        prestamo = self.prestamos.buscar_activo(id_socio, id_libro)
        if not prestamo:
            raise ValueError("No hay préstamo activo")
        self.prestamos.devolver(prestamo["id"])
        self.libros.cambiar_disponible(id_libro, 1)
