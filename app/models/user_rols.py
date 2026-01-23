from app.models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

class UserRol(Base):
    __tablename__ = "user_rols"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    rol_id: Mapped[int] = mapped_column(ForeignKey("rols.id"))

    user: Mapped["User"] = relationship(
        back_populates="user_rols",
        overlaps="users,rols"
    )
    rol: Mapped["Rol"] = relationship(
        back_populates="rol_users",
        overlaps="user_rols,users"
    )

