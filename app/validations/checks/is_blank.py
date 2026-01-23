def is_blank(value: str | None) -> bool:
    return not value or not value.strip()
