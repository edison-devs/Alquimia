from app.models import Base
from app.models.abstracts.datetime_mixin import CreatedAtMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import datetime

class Session(Base, CreatedAtMixin):
    __tablename__ = "sessions"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    expires_at: Mapped[datetime]
    is_active: Mapped[bool] = mapped_column(default=True)

    user: Mapped["User"] = relationship("User", 
        back_populates="sessions",         
        lazy="selectin",
    )

    def __str__(self):
        parts = [
            f"Session(user_id={self.user_id})",
            f"Activo={'Sí' if self.is_active else 'No'}",
            f"Expira={self.expires_at.strftime('%Y-%m-%d %H:%M:%S')}"
        ]
        return " | ".join(parts)