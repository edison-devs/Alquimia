def has_errors(data: object):
    if not isinstance(data, dict):
        return False

    return any(
        key in data and isinstance(data[key], (list, dict))
        for key in ("error", "conflict", "validations")
    )
