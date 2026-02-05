# Alquimia Backend Template

Este proyecto es una base estándar de backend escrita en Python utilizando SQLAlchemy como ORM. Ha sido simplificado para servir como una plantilla base que incluye la gestión esencial de usuarios, roles y sesiones.

## Características Principales

- **Gestión de Usuarios**: Registro, login y perfiles básicos.
- **Roles y Permisos**: Sistema de roles (admin, employee, observer) vinculado a usuarios.
- **Sesiones**: Seguimiento de sesiones activas con expiración.
- **ORM SQLAlchemy**: Modelado de base de datos relacional moderno.
- **Mixins Reutilizables**: Soft delete, timestamps automáticos y gestión de contraseñas.

## Requisitos

- Python 3.x
- MariaDB/MySQL (o cualquier dialecto compatible con SQLAlchemy)
- Dependencias listadas en `requirements.txt`

## Configuración Inicial

1. **Instalar Dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Variables de Entorno**:
   Copia el archivo `.env.example` a `.env` y configura tus credenciales de base de datos:
   ```env
   USER=tu_usuario
   PASSWORD=tu_contrasena
   HOST=localhost
   PORT=3306
   DATABASE=alquimia_db
   DIALECT=mysql
   DRIVER=mysqlclient
   ```

3. **Migraciones**:
   Este proyecto utiliza Alembic para la gestión de migraciones:
   ```bash
   alembic upgrade head
   ```

4. **Semillas (Seeders)**:
   Para poblar la base de datos con roles iniciales y un usuario administrador predeterminado:
   ```bash
   python runner.py seeders
   ```

## Comandos Disponibles

El archivo `runner.py` centraliza la ejecución de tareas comunes:

- `python runner.py init`: Inicia la interfaz de usuario (basada en wxPython).
- `python runner.py seeders`: Ejecuta todos los seeders (roles y usuario admin).
- `python runner.py seed_roles`: Solo siembra los roles iniciales.
- `python runner.py seed_default_user`: Crea el usuario root/admin.
- `python runner.py test`: Ejecuta una prueba simple de cierre de sesión.

## Estructura del Proyecto

- `app/`: Lógica principal de la aplicación.
  - `models/`: Definiciones de tablas y relaciones.
  - `controllers/`: Lógica de negocio (sesiones, usuarios).
  - `validations/`: Lógica de validación de datos.
  - `views/`: Interfaz gráfica (wxPython).
  - `seeders/`: Scripts para poblar la base de datos.
- `config/`: Configuraciones de base de datos y esquemas.
- `migrations/`: Historial de cambios en la base de datos (Alembic).


## 📚 Documentación

En la carpeta `docs/` encontrarás guías detalladas:

- **[🏠 Arquitectura](docs/ARCHITECTURE.md)**: Estructura técnica y patrones.
- **[🗄️ Base de Datos](docs/DATABASE.md)**: Modelos core (User, Rol, Session).
- **[👨‍💻 Guía de Desarrollador](docs/DEVELOPER.md)**: Cómo extender la plantilla.
- **[📖 Manual de Usuario](docs/USER_MANUAL.md)**: Uso básico del sistema.

Para más detalles técnicos, consulta [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).
