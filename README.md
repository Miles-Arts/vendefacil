# Vende-Fácil

Vende-Fácil es una aplicación desarrollada para facilitar la conexión entre vendedores de productos agrícolas y compradores de alimentos del campo. Su propósito principal es actuar como intermediaria digital, permitiendo la gestión eficiente de ventas, compras, productos y usuarios dentro del ecosistema agrícola.

## Índice
- [Descripción del Proyecto](#descripción-del-proyecto)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Instalación y Configuración](#instalación-y-configuración)
- [Inicialización del Proyecto](#inicialización-del-proyecto)
- [Conexión a la Base de Datos PostgreSQL](#conexión-a-la-base-de-datos-postgresql)
- [Solución a Errores Comunes](#solución-a-errores-comunes)
- [Metodología de Trabajo](#metodología-de-trabajo)
- [Arquitectura del Proyecto](#arquitectura-del-proyecto)
- [Versión del Proyecto](#versión-del-proyecto)
- [Autor e Institución](#autor-e-institución)
- [Licencia](#licencia)

## Descripción del Proyecto
Vende-Fácil maneja distintos tipos de usuarios (clientes y vendedores), así como el registro de productos con sus características específicas (tipo, tamaño, precio, disponibilidad). También permite realizar ventas y compras, y relacionarlas con los productos comercializados.

## Proyecto educativo

Este proyecto es exclusivamente para fines de aprendizaje y corresponde a un proyecto de estudios del programa Tecnólogo en Análisis y Desarrollo de Software del SENA. No debe ser utilizado en producción ni para fines comerciales.

## Tecnologías Utilizadas
### Backend
- Python (Flask)
- JSON
- PostgreSQL
- Jinja2
- ENV o VENV
- Postman

### Frontend
- HTML
- CSS
- JavaScript
- Bootstrap

### Herramientas de Desarrollo
- Git
- GitHub
- Visual Studio Code
- Copilot Pro
- Canva
- Creadores de UML

### Sistema Operativo
- Windows 11

## Instalación y Configuración
### Instalación de Python
1. Descarga Python desde su [sitio oficial](https://www.python.org/downloads/).
2. Durante la instalación, asegúrate de marcar la opción "Add Python to PATH".
3. Verifica la instalación ejecutando:
   ```bash
   python --version
   # o
   python3 --version
   ```

### Instalación de Virtualenv
1. Instala virtualenv utilizando pip:
   ```bash
   pip install virtualenv
   ```
2. Crea un entorno virtual con Python 3:
   ```bash
   python -m virtualenv venv
   ```
3. Activa el entorno virtual:
   - En Windows (Git Bash):
     ```bash
     source venv/Scripts/activate
     ```
   - En Windows (PowerShell o CMD):
     ```bash
     .\venv\Scripts\activate
     ```
   - En Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
4. Verifica si el entorno virtual está activo:
   - En Bash:
     ```bash
     echo $VIRTUAL_ENV
     ```
   - En PowerShell:
     ```powershell
     $env:VIRTUAL_ENV
     ```

### Instalación de Flask y Herramientas Adicionales
Asegúrate de estar dentro del entorno virtual antes de ejecutar estos comandos:
```bash
pip install flask setuptools wheel
pip install flask-cors
pip install python-decouple
pip install python-dotenv
```

### Dependencias Adicionales
Para conectar la aplicación con PostgreSQL:
```bash
pip install psycopg2
# o para evitar problemas de compilación
pip install psycopg2-binary
```

## Inicialización del Proyecto
1. Asegúrate de estar en la carpeta raíz del proyecto.
2. Ejecuta el siguiente comando para iniciar el servidor Flask:
   ```bash
   py ./src/utils/app.py
   ```
3. Abre tu navegador y visita [http://127.0.0.1:5000](http://127.0.0.1:5000) para verificar que el servidor esté corriendo.

## Conexión a la Base de Datos PostgreSQL
- Host: localhost
- Usuario: postgres
- Contraseña: 1234
- Base de datos: VendeFacil
- Puerto: 5432

La conexión se realiza usando SQLAlchemy y psycopg2. Ejemplo de configuración en `app.py`:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/VendeFacil'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```
Para verificar la conexión, ejecuta:
```bash
python src/conexion_postgresql.py
```

## Solución a Errores Comunes
- Verifica las rutas en el navegador.
- Cierra y abre Visual Studio Code si los cambios no se reflejan.
- Actualiza la página web con Ctrl + F5.
- Reinicia el servidor local si es necesario.
- Cierra y abre una nueva terminal si el entorno virtual no funciona correctamente.

## Metodología de Trabajo
Este proyecto utiliza la metodología **Kanban** para la gestión y organización de tareas. Kanban permite visualizar el flujo de trabajo, identificar cuellos de botella y mejorar la eficiencia del equipo.

## Arquitectura del Proyecto
El proyecto utiliza una arquitectura MVC (Modelo-Vista-Controlador):

- El **Modelo (Model)** gestiona la lógica de datos y la conexión a la base de datos (por ejemplo, archivos como `src/conexion_postgresql.py`).
- La **Vista (View)** corresponde a la interfaz de usuario, ubicada en la carpeta `templates/` con archivos HTML.
- El **Controlador (Controller)** maneja la lógica de la aplicación y las rutas, como en `app.py`.

Esta arquitectura permite separar responsabilidades, facilitando el mantenimiento y la escalabilidad del proyecto.

## Versión del Proyecto
Actualmente en la versión **0.0.1** (etapa temprana de desarrollo). Se sigue el esquema de versionado semántico.

## Autor e Institución
- **Autor:** Milton Figueredo ([LinkedIn](#) | [GitHub](#))
- **Institución:** SENA - Servicio Nacional de Aprendizaje
- **Programa:** Tecnólogo en Análisis y Desarrollo de Software
- **Fecha:** Mayo 2025

## Licencia
Este proyecto está licenciado bajo la Licencia MIT.

---

© 2025 Milton Figueredo

