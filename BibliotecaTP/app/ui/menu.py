class Menu:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def iniciar(self):
        while True:
            print("\n=== Menú Biblioteca ===")
            print("1. Libros")
            print("2. Socios")
            print("3. Préstamos")
            print("4. Salir")
            op = input("Elija opción: ")
            if op == "1":
                self.menu_libros()
            elif op == "2":
                self.menu_socios()
            elif op == "3":
                self.menu_prestamos()
            elif op == "4":
                print("Gracias por usar el sistema bibliotecario. Lo esperamos pronto.")
                break
            else:
                print("Opción inválida")

    def menu_libros(self):
        while True:
            print("\n--- Menú Libros ---")
            print("1. Listar libros disponibles")
            print("2. Listar todos los libros")
            print("3. Agregar libro")
            print("4. Volver al menú principal")
            op = input("Opción: ")
            if op == "1":
                print("\nLibros disponibles:")
                libros = self.biblioteca.libros.listar_disponibles()
                if libros:
                    for l in libros:
                        print(f"{l['id']}: {l['titulo']} ({l['autor']})")
                else:
                    print("No hay libros disponibles.")
            elif op == "2":
                print("\nTodos los libros:")
                libros = self.biblioteca.libros.listar_todos()
                if libros:
                    for l in libros:
                        estado = "Disponible" if l["disponible"] else "Prestado"
                        print(f"{l['id']}: {l['titulo']} ({l['autor']}) - {estado}")
                else:
                    print("No hay libros registrados.")
            elif op == "3":
                print("\nAgregar un nuevo libro:")
                t = input("Título: ")
                a = input("Autor: ")
                id_libro = self.biblioteca.agregar_libro(t, a)
                print(f"Libro agregado con ID {id_libro}")
            elif op == "4":
                break
            else:
                print("Opción inválida")

    def menu_socios(self):
        while True:
            print("\n--- Menú Socios ---")
            print("1. Listar socios")
            print("2. Agregar socio")
            print("3. Volver al menú principal")
            op = input("Opción: ")
            if op == "1":
                print("\nLista de socios:")
                socios = self.biblioteca.socios.listar()
                if socios:
                    for s in socios:
                        print(f"{s['id']}: {s['nombre']} ({s['email']})")
                else:
                    print("No hay socios registrados.")
            elif op == "2":
                print("\nAgregar un nuevo socio:")
                n = input("Nombre: ")
                e = input("Email: ")
                id_socio = self.biblioteca.agregar_socio(n, e)
                print(f"Socio agregado con ID {id_socio}")
            elif op == "3":
                break
            else:
                print("Opción inválida")

    def menu_prestamos(self):
        while True:
            print("\n--- Menú Préstamos ---")
            print("1. Prestar libro")
            print("2. Devolver libro")
            print("3. Listar préstamos activos")
            print("4. Volver al menú principal")
            op = input("Opción: ")

            if op == "1":
                print("\nPrestar un libro:")
                try:
                    id_socio = int(input("ID del socio: "))
                    id_libro = int(input("ID del libro: "))
                    id_prestamo = self.biblioteca.prestar_libro(id_socio, id_libro)
                    print(f"Préstamo realizado con ID {id_prestamo}")
                except Exception as e:
                    print("Error:", e)

            elif op == "2":
                print("\nDevolver un libro:")
                try:
                    id_socio = int(input("ID del socio: "))
                    id_libro = int(input("ID del libro: "))
                    self.biblioteca.devolver_libro(id_socio, id_libro)
                    print("Libro devuelto correctamente")
                except Exception as e:
                    print("Error:", e)

            elif op == "3":
                print("\nPréstamos activos:")
                prestamos = self.biblioteca.prestamos.listar_activos()
                if not prestamos:
                    print("No hay préstamos activos.")
                else:
                    for p in prestamos:
                        socio = self.biblioteca.socios.obtener(p["id_socio"])
                        libro = self.biblioteca.libros.obtener(p["id_libro"])
                        nombre_socio = socio["nombre"] if socio else "Desconocido"
                        titulo_libro = libro["titulo"] if libro else "Desconocido"
                        print(f"Préstamo {p['id']}: Socio {p['id_socio']} ({nombre_socio}) - Libro {p['id_libro']} ('{titulo_libro}')")

            elif op == "4":
                break
            else:
                print("Opción inválida")

