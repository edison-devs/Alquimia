# Arquitectura del Estándar Alquimia 2.0

## Visión General

Alquimia 2.0 es una plantilla base para el desarrollo de aplicaciones de escritorio con backend en Python. Su objetivo es proporcionar una estructura limpia, modular y escalable que incluya "out of the box" las funcionalidades esenciales de cualquier sistema administrativo: autenticación, gestión de usuarios y roles.

## Tecnologías Principales

- **Lenguaje**: Python 3.10+
- **Interfaz Gráfica (GUI)**: wxPython
- **ORM**: SQLAlchemy 2.0+
- **Base de Datos**: Compatible con MySQL/MariaDB (configurable)
- **Migraciones**: Alembic
- **Validación**: Pydantic

## Estructura MVC

El proyecto implementa el patrón **Modelo-Vista-Controlador**:

### 1. Modelos (`app/models`)
Representan la capa de datos.
- Heredan de `Base` (DeclarativeBase).
- Utilizan **Mixins** ubicados en `app/models/abstracts` para reutilizar código (ej. `SoftDeleteMixin` para borrado lógico, `DateTimeMixin` para auditoría temporal).

### 2. Vistas (`app/views`)
Responsables de la presentación. Construidas con la librería `wxPython`.
- La aplicación inicia en `app/views/components/my_app.py`.

### 3. Controladores (`app/controllers`)
Mandan sobre la lógica de negocio.
- `UserController`: Gestión de usuarios (CRUD, asignación de roles).
- `SessionController`: Manejo de login/logout y sesiones activas.

## Flujo de Ejecución

1. El usuario ejecuta `python runner.py init`.
2. Se cargan las configuraciones de entorno (`.env`).
3. Se inicializa el motor de base de datos (`settings.py`).
4. Se lanza el loop principal de la GUI (`wx.App`).

## Directorios Clave

```
alquimia_2.0/
├── app/
│   ├── controllers/   # Lógica de negocio
│   ├── models/        # Definiciones de tablas
│   ├── views/         # Ventanas y componentes gráficos
│   └── seeders/       # Datos iniciales (admin, roles)
├── config/            # Configuraciones globales
├── docs/              # Esta documentación
├── migrations/        # Historial de cambios de BD
├── runner.py          # CLI Runner
└── commands.py        # Registro de comandos CLI
```
