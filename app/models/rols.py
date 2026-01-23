from app.models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

class Rol(Base):
    __tablename__ = "rols"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)

    rol_users: Mapped[list["UserRol"]] = relationship(
        "UserRol",
        back_populates="rol",
        overlaps="users"
    )
    users: Mapped[list["User"]] = relationship(
        "User",
        secondary="user_rols",
        back_populates="rols",
        overlaps="user_rols"
    )

