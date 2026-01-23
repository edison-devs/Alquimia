from settings import SessionLocal
from sqlalchemy.orm import selectinload

def reload(obj, *rels):
    cls = obj.__class__
    invalid = [r for r in rels if not hasattr(cls, r)]

    if invalid:
        raise AttributeError(f"Relaciones no válidas en {cls.__name__}: {invalid}")

    with SessionLocal() as s:
        return (
            s.query(cls)
            .options(*[selectinload(getattr(cls, r)) for r in rels])
            .get(obj.id)
        )

