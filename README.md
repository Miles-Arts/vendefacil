# Vende-Fácil

Vende-Fácil es una aplicación desarrollada para facilitar la conexión entre vendedores de productos agrícolas y compradores de alimentos del campo. Su propósito principal es actuar como intermediaria digital, permitiendo la gestión eficiente de ventas, compras, productos y usuarios dentro del ecosistema agrícola.

## Índice
- [Descripción del Proyecto](#descripción-del-proyecto)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Instalación y Configuración](#instalación-y-configuración)
- [Inicialización del Proyecto](#inicialización-del-proyecto)
- [Conexión a la Base de Datos PostgreSQL](#conexión-a-la-base-de-datos-postgresql)
- [Configuración de variables de entorno](#configuración-de-variables-de-entorno)
- [Solución a Errores Comunes](#solución-a-errores-comunes)
- [Metodología de Trabajo](#metodología-de-trabajo)
- [Arquitectura del Proyecto](#arquitectura-del-proyecto)
- [Versión del Proyecto](#versión-del-proyecto)
- [Autor e Institución](#autor-e-institución)
- [Licencia](#licencia)

## Comandos Especiales de Agent Mode

Domina estos comandos especiales para potenciar tu experiencia con Agent Mode:

- **/tools** - Muestra una lista completa de herramientas disponibles con descripciones de cada una.
  - Ejemplo: `/tools` revela que Agent Mode puede acceder a comandos git, operaciones de terminal y extensiones de VS Code.

- **/clear** - Inicia una conversación limpia con un nuevo contexto.
  - Ejemplo: Después de trabajar en un componente React, usa `/clear` antes de cambiar a trabajo de API backend.

- **/help [tema]** - Obtén ayuda detallada sobre funciones específicas de Agent Mode.
  - Ejemplo: `/help file-operations` muestra todas las formas en que Agent Mode puede manipular archivos.

- **/focus [carpeta]** - Restringe Agent Mode para trabajar solo con archivos en un directorio específico.
  - Ejemplo: `/focus src/componentes` limita el contexto a esa carpeta.

- **/contexto [archivo]** - Añade archivos específicos como contexto para tu próxima solicitud.
  - Ejemplo: `/contexto package.json` asegura que Agent Mode entienda tus dependencias.


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

> **Nota:** Para retornar respuestas en formato JSON en tus rutas, debes importar `jsonify` desde Flask:
> ```python
> from flask import jsonify
> ```

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

## Importar request de Flask

Para manejar datos enviados en peticiones HTTP (por ejemplo, para recibir datos en rutas POST), debes importar el objeto `request` de Flask:

```python
from flask import request
```

Esto te permite acceder a los datos enviados por el cliente usando `request.json`, `request.form`, etc.

## Formateo de Fechas en Python

Para organizar y manipular fechas solo en números (por ejemplo, YYYY-MM-DD), puedes usar el módulo `datetime` de Python. Ejemplo de uso:

```python
import datetime

fecha_actual = datetime.datetime.now()
fecha_formateada = fecha_actual.strftime('%Y-%m-%d')
print(fecha_formateada)  # Salida: 2025-05-14
```

Esto es útil para guardar fechas en bases de datos o mostrar fechas en un formato estándar.

## Configuración de variables de entorno

Antes de ejecutar la aplicación, debes crear una carpeta llamada `.env` en la raíz del proyecto. Dentro de esta carpeta, crea un archivo para definir las variables de entorno necesarias para la conexión a la base de datos y la seguridad de la aplicación. Ejemplo de variables que debes agregar:

```
SECRET_KEY=tu_clave_secreta
PGSQL_HOST=localhost
PGSQL_USER=postgres
PGSQL_PASSWORD=tu_contraseña
PGSQL_DATABASE=VendeFacil
```

Asegúrate de no compartir este archivo ni sus datos sensibles en repositorios públicos.

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
- La **Controlador (Controller)** maneja la lógica de la aplicación y las rutas, como en `app.py`.

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

