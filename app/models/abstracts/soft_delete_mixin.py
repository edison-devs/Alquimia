import bcrypt
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime
from datetime import datetime

class SoftDeleteMixin:
    deleted_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=None, nullable=True)

    def soft_delete(self) -> None:
        self.deleted_at = datetime.now()

    def restore(self) -> None:
        self.deleted_at = None