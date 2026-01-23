from pydantic import ValidationError
from datetime import datetime, timezone, timedelta
from settings import SessionLocal

from app.models.sessions import Session
from app.models.users import User
from app.models.rols import Rol

from app.validations.login_validations import LoginValidation
from app.mixins.formats_validations import formats_validations
from app.mixins.has_errors import has_errors

class SessionController:

#-------------------------------------------------------------------------
    def create_session(self, user_id) -> Session | dict:
        try:
            session = SessionLocal()
            new_session = Session(
                user_id=user_id,
                expires_at=datetime.now(timezone.utc) + timedelta(hours=48),
                is_active=True
            )
            session.add(new_session)
            session.commit()
            session.refresh(new_session)
            session.expunge(new_session)
            return new_session
        except Exception as e:
            session.rollback()
            return {
                "error": [
                    str(e),
                    "session_controler.create_session: Error al crear sesión."
                ]
            }
        finally:
            session.close()

    def update_session(self, user_session) -> Session | dict:
        try:
            session = SessionLocal()
            user_session.is_active = True
            user_session.expires_at = datetime.now(timezone.utc) + timedelta(hours=2)
            merged = session.merge(user_session)  # ← este sí pertenece a esta sesión
            session.commit()
            session.refresh(merged)
            session.expunge(merged)
            return merged
        except Exception as e:
            session.rollback()
            return {
                "error": [
                    str(e),
                    "session_controler.update_session: Error al actualizar sesión."
                ]
            }
        finally:
            session.close()

    def activate_session(self, user_id) -> Session | dict:
        try:
            session = SessionLocal()
            user_session = session.query(Session).filter_by(user_id=user_id).first()
            session.commit()
            session.close()

            if not user_session:
                return self.create_session(user_id)

            # Si está activa, actualízala igual
            return self.update_session(user_session)

        except Exception as e:
            return {
                "error": [
                    str(e),
                    "session_controler.activate_session: Error al activar sesión."
                ]
            }

    def login(self, **kwargs) -> Session | dict:
        try:
            data = LoginValidation(**kwargs)
        except ValidationError as e:
            return {'validations': formats_validations(e)}

        session = SessionLocal()
        try:
            user = session.query(User).filter(User.username == data.username).first()
            if not user or not user.verify_password(data.password):
                return {'conflict': ["Credenciales inválidas."]}

            new_session = self.activate_session(user.id)
            
            if has_errors(new_session):
                return new_session
            
            return new_session

        except Exception as e:
            return {
                "error": [
                    str(e),
                    "session_controller.login: Error al iniciar sesión."
                ]
            }
        finally:
            session.close()

    def logout(self, user_id) -> Session |dict:
        try:
            session = SessionLocal()
            active_session = session.query(Session).filter_by(user_id=user_id, is_active=True).first()
            if not active_session:
                return {"conflict": ["No hay sesión activa para este usuario."]}
            
            active_session.is_active = False
            session.commit()
            session.refresh(active_session)
            session.expunge(active_session)     
            
            return active_session
        except Exception as e:
            session.rollback()
            return {
                "error": [
                    str(e),
                    "session_controller.logout: Error al cerrar sesión."
                ]
            }
        finally:
            session.close()
    #-------------------------------------------------------------------------
    def validate_activate_session(self) -> User | dict:
        session = SessionLocal()
        try:
            active_session = session.query(Session).filter_by(is_active=True).first()
            if not active_session:
                return {"conflict": ["No hay sesiones activas."]}
            
            now = datetime.now(timezone.utc)
            expires_at = active_session.expires_at
            # Si expires_at es naive, hazlo aware en UTC
            if expires_at.tzinfo is None:
                expires_at = expires_at.replace(tzinfo=timezone.utc)
            
            if expires_at < now:
                active_session.is_active = False
                session.commit()
                return {"conflict": ["La sesión ha expirado y se ha cerrado."]}
            
            session.commit()
            user = session.get(User, active_session.user_id)
            session.refresh(active_session)
            session.expunge(user)
            return user

        except Exception as e:
            session.rollback()
            return {
                "error": [
                    str(e),
                    "session_controler.validate_activate_session: Error al validar la sesión."
                ]
            }
        finally:
            session.close()