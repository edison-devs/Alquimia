from pydantic import ValidationError
import re

def formats_validations(e: ValidationError) -> dict[str, list[str]]:
    errors: dict[str, list[str]] = {}
    
    for err in e.errors():
        field = err["loc"][0]
        raw_msg = err["msg"]
        
        if ", " in raw_msg:
            raw_msg = raw_msg.split(", ", 1)[1]
            
        split_msgs = [msg.strip() for msg in re.split(r"[.,]", raw_msg) if msg.strip()]
        errors.setdefault(field, []).extend(split_msgs)
    return errors
