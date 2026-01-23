from pydantic import BaseModel, field_validator

from typing import Optional

from app.validations.checks.is_blank import is_blank
from app.validations.checks.has_space import has_space
from app.validations.checks.is_alpha import is_alpha
from app.validations.checks.is_email import is_email

class UserValidation(BaseModel):
    name: str
    last_name: str
    username: str
    email: str
    phone: Optional[str]
    password: str

    @field_validator("name")
    def name_valid(cls, name):
        validations = []
        if  is_blank(name):
            validations.append("El nombre no puede estar en blanco")
        if has_space(name):
            validations.append("El nombre no debe contener espacios")
        if not is_alpha(name):
            validations.append("El nombre solo debe contener letras sin símbolos ni números")
        if validations:
            raise ValueError(", ".join(validations))
        return name

    @field_validator("last_name")
    def last_name_valid(cls, last_name):
        validations = []
        if  is_blank(last_name):
            validations.append("El apellido no puede estar en blanco")
        if has_space(last_name):
            validations.append("El apellido no debe contener espacios")
        if not is_alpha(last_name):
            validations.append("El apellido solo debe contener letras sin símbolos ni números")
        if validations:
            raise ValueError(", ".join(validations))
        return last_name

    @field_validator("username")
    def username_valid(cls, username):
        validations = []
        if  is_blank(username):
            validations.append("El nombre de usuario no puede estar en blanco")
        if has_space(username):
            validations.append("El nombre de usuario no debe contener espacios")
        if validations:
            raise ValueError(", ".join(validations))
        return username

    @field_validator("email")
    def email_valid(cls, email):
        email = email.strip()
        validations = []
        if  is_blank(email):
            validations.append("El correo no puede estar en blanco")
        if not is_email(email):
            validations.append("El correo no tiene un formato válido")
        if has_space(email):
            validations.append("El email no debe contener espacios")
        if validations:
            raise ValueError(", ".join(validations))
        return email

    @field_validator("phone")
    def phone_valid(cls, phone):
        validations = []
        if is_blank(phone):
            return None
        if not phone.isdigit():
            validations.append("Debe contener solo dígitos")
        if len(phone) < 10:
            validations.append("Debe tener al menos 10 dígitos")
        if validations:
            raise ValueError(", ".join(validations))
        return phone

    @field_validator("password")
    def password_valid(cls, password):
        validations = []
        if len(password) < 8:
            validations.append("Debe tener al menos 8 caracteres")
        if not any(c.isdigit() for c in password):
            validations.append("Debe contener al menos un número")
        if not any(c.isalpha() for c in password):
            validations.append("Debe contener al menos una letra")
        if validations:
            raise ValueError(", ".join(validations))
        return password
