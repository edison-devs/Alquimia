from settings import SessionLocal
from app.models.rols import Rol
from app.models.users import User
from sqlalchemy.exc import IntegrityError

def seeders():
    seed_roles()
    seed_default_user()

def seed_roles():
    role_names = ["observer", "employee", "admin"]

    with SessionLocal() as session:
        for name in role_names:
            exists = session.query(Rol).filter_by(name=name).first()
            if not exists:
                session.add(Rol(name=name))
        try:
            session.commit()
            print("Roles base sembrados correctamente.")
        except IntegrityError as e:
            session.rollback()
            print(f"Error al sembrar roles: {e}")

def seed_default_user():
    with SessionLocal() as session:
        # Verifica si el usuario ya existe por username o email
        username = "admin"
        email = "admin@example.com"
        user = session.query(User).filter((User.username == username) | (User.email == email)).first()
        if not user:
            user = User(
                name="Root",
                last_name="root",
                username=username,
                email=email,
                phone="000000000",
                password="Admin1234"
            )
            session.add(user)
            session.commit()
            session.refresh(user)
        
        # Asigna los 3 roles al usuario
        roles = session.query(Rol).filter(Rol.name.in_(["observer", "employee", "admin"])).all()
        for rol in roles:
            if rol not in user.rols:
                user.rols.append(rol)
        try:
            session.commit()
            print("Usuario predeterminado creado con los 3 roles.")
        except IntegrityError as e:
            session.rollback()
            print(f"Error al crear usuario predeterminado: {e}")
