# Guía de Desarrollador

Esta plantilla está diseñada para ser extendida. Aquí se explica cómo empezar y cómo agregar nuevas funcionalidades.

## Setup Inicial

1. **Instalar Dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Configurar Entorno**:
   Crea un archivo `.env` basado en `.env.example`.
3. **Base de Datos**:
   Asegúrate de que tu servidor MySQL esté corriendo y la BD vacía exista.
   ```bash
   alembic upgrade head
   python runner.py seeders
   ```

## Workflow de Desarrollo

### Agregar un Nuevo Modelo
Para añadir una nueva entidad (por ejemplo, `Producto`):

1. Crea `app/models/product.py`.
2. Define la clase heredando de `Base` y los mixins necesarios.
   ```python
   from app.models import Base
   from app.models.abstracts.soft_delete_mixin import SoftDeleteMixin
   
   class Product(Base, SoftDeleteMixin):
       __tablename__ = "products"
       # ... columnas ...
   ```
3. Importa el nuevo modelo en `app/models/__init__.py` (Crítico para que Alembic lo vea).
4. Genera la migración:
   ```bash
   alembic revision --autogenerate -m "add_products_table"
   alembic upgrade head
   ```

### Crear Comandos Personalizados
Puedes registrar tus propios scripts en `commands.py` para ejecutarlos con `runner.py`.

```python
# commands.py
def mi_script():
    print("Hola Mundo")

commands = {
    # ...
    "saludar": mi_script
}
```
Ejecutar con: `python runner.py saludar`

## Tests
El comando `python runner.py test` ejecuta una suite básica de pruebas definidas en `commands.py`. Se recomienda expandir esto usando `pytest`.
