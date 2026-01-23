from app.models import Base
from app.models.abstracts.datetime_mixin import DateTimeMixin
from app.models.abstracts.soft_delete_mixin import SoftDeleteMixin
from app.models.abstracts.password_mixin import PasswordMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

class User(Base, PasswordMixin, DateTimeMixin, SoftDeleteMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(30), nullable=True)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    user_rols: Mapped[list["UserRol"]] = relationship("UserRol", back_populates="user")
    sessions: Mapped[list["Session"]] = relationship("Session", back_populates="user")
    rols: Mapped[list["Rol"]] = relationship(
        "Rol",
        secondary="user_rols",
        back_populates="users",
        lazy="selectin",
        overlaps="rol_users,user_rols,rol"
    )
    
    def __str__(self):
        parts = [f"User(nombre='{self.name}')"]

        if self.rols:
            rol_names = ", ".join([rol.name for rol in self.rols])
            parts.append(f"Rols=[{rol_names}]")

        return " | ".join(parts)


