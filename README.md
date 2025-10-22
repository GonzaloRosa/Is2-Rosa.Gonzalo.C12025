# 📚 Sistema de Gestión de Biblioteca

Este proyecto es un **sistema de gestión para bibliotecas**, desarrollado con **Python** y organizado en una **arquitectura por capas**.  
Permite gestionar libros, socios y préstamos mediante menús en consola.

---

## 🧩 Arquitectura del Sistema

El proyecto sigue una **arquitectura en tres capas**:

1. **Capa de Presentación (UI)**  
   Contiene los menús y la interacción con el usuario.  
   - Archivo: `menu.py`
   - Carpeta: `dominio/`

2. **Capa de Lógica de Negocio (Business Logic)**  
   Define las clases principales y las reglas de negocio del sistema (biblioteca, préstamos, validaciones).  
   - Archivo: `biblioteca.py`
   - Carpeta: `dominio/`

3. **Capa de Acceso a Datos (DAL - Data Access Layer)**  
   Gestiona la conexión con la base de datos y las operaciones CRUD (crear, leer, actualizar, eliminar).  
   - Carpeta: `db/`
   - Archivos:  
     - `conexion.py` → Maneja la conexión SQLite  
     - `libros_dal.py` → Operaciones sobre libros  
     - `socios_dal.py` → Operaciones sobre socios  
     - `prestamos_dal.py` → Operaciones sobre préstamos  

---

## Estructura del Proyecto

BibliotecaTP/  
├─ app/  
│ ├─ business/  
│ │ └─ domain/  
│ │ ├─ **init**.py  
│ │ └─ biblioteca.py  
│ │  
│ ├─ dal/  
│ │ ├─ db/  
│ │ │ └─ models/  
│ │ │ ├─ libros_dal.py  
│ │ │ ├─ socios_dal.py  
│ │ │ └─ prestamos_dal.py  
│ │ ├─ **init**.py  
│ │ └─ conexion.py  
│ │  
│ ├─ ui/  
│ │ └─ menu.py  
│ │  
│ ├─ main.py  
│ └─ data/  
│ └─ biblioteca.db ← Se genera automáticamente  
│  
├─ docs/  
│ ├─ Diagrama UML Biblioteca.png  
│ └─ is2-Rosa.Gonzalo.C1.2025.docx  
│  
├─ venv/ ← Entorno virtual de Python  
└─ README.md`









