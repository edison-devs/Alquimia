
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base() #alquemist declarative form 2.0 

from sqlalchemy.orm import DeclarativeBase
import importlib
import pkgutil
class Base(DeclarativeBase): #alquemist declarative form 2.0+
    pass

def auto_import_models():
    package = __import__(__name__)
    for _, name, _ in pkgutil.iter_modules(__path__):
        importlib.import_module(f"{__name__}.{name}")

# Ejecutar importación automática al cargar el paquete
auto_import_models()

