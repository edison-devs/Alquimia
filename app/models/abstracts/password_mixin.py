import bcrypt
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

class PasswordMixin:
    _password: Mapped[str] = mapped_column("password", String(128), nullable=False)

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, plain_password: str) -> None:
        hashed = bcrypt.hashpw(plain_password.encode("utf-8"), bcrypt.gensalt())
        self._password = hashed.decode("utf-8")

    def verify_password(self, intentado: str) -> bool:
        return bcrypt.checkpw(intentado.encode("utf-8"), self._password.encode("utf-8"))