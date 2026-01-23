import re

def is_alpha(value: str) -> bool:
    return bool(re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ]+$", value))