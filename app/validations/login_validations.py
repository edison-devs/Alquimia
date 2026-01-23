from pydantic import BaseModel, field_validator


from app.validations.checks.is_blank import is_blank
from app.validations.checks.has_space import has_space


class LoginValidation(BaseModel):
    username: str
    password: str

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