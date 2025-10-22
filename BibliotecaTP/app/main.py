from dal.db.conexion import ConexionBD
from dal.db.models.libros_dal import LibrosDAL
from dal.db.models.socios_dal import SociosDAL
from dal.db.models.prestamos_dal import PrestamosDAL
from business.domain.biblioteca import Biblioteca
from ui.menu import Menu

# Inicializar BD
conn = ConexionBD.get_instancia().conn

# Crear DAL
libros = LibrosDAL(conn)
socios = SociosDAL(conn)
prestamos = PrestamosDAL(conn)

# Lógica de negocio
biblio = Biblioteca(libros, socios, prestamos)

# Menú
menu = Menu(biblio)
menu.iniciar()
