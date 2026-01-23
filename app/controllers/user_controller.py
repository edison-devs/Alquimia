from pydantic import ValidationError
from datetime import datetime, timezone, timedelta

from settings import SessionLocal

from app.models.users import User
from app.models.rols import Rol
from app.models.sessions import Session

from app.validations.user_validations import UserValidation
from app.validations.login_validations import LoginValidation
from app.mixins.formats_validations import formats_validations
from app.mixins.has_errors import has_errors

class UserController:

    def create(self, **kwargs) -> User | dict:
        try:
            data = UserValidation(**kwargs)
        except ValidationError as e:
            return {'validations': formats_validations(e)}

        session = SessionLocal()
        try:
            if session.query(User).filter(User.username == data.username).first():
                return {'conflict': {"username": ["El nombre de usuario ya está registrado."]}}
            if session.query(User).filter(User.email == data.email).first():
                return {'conflict': {"email": ["El correo ya está registrado."]}}

            new_user = User(
                name=data.name,
                last_name=data.last_name,
                username=data.username,
                email=data.email,
                phone=data.phone
            )
            new_user.password = data.password

            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            session.expunge(new_user)
            return new_user

        except Exception as e:
            try:
                session.rollback()
            except Exception:
                pass
            return {
                "error": [
                    str(e),
                    "user_controller.create: Error al crear el usuario."
                ]
            }
        finally:
            session.close()

    def register(self, **kwargs) -> User | dict:
        data = self.create(**kwargs)
        if has_errors(data):
            return data

        session = SessionLocal()
        try:
            new_user = session.get(User, data.id)
            if not new_user: 
                raise Exception(f"Usuario con ID {data.id} no encontrado tras creación.")

            observer_rol = session.query(Rol).filter(Rol.name == "observer").first()
            if not observer_rol:
                session.delete(new_user)
                session.commit()
                raise Exception("Rol 'observer' no existe en la base de datos.")
            
            new_user.rols.append(observer_rol)
            session.commit()
            session.refresh(new_user)
            session.expunge(new_user)
            return new_user

        except Exception as e:
            try:
                session.rollback()
            except Exception:
                pass
            return {
                "error": [
                    str(e),
                    f"user_controller.register: Error al registrar el usuario."
                ]
            }
        finally:
            session.close()
