import re
from pydantic import ValidationError, validator

def validate_text_fields(value):
    if value is None:
        return value
    pattern = r'^[\w\s\dąćęłńóśźżĄĆĘŁŃÓŚŹŻ\-,.()/\'"]+(\s\(N\\Ż\))?$'
    if not re.match(pattern, value):
        raise ValueError('Invalid text format')
    return value

def validate_id(value):
    if not isinstance(value, int) or value < 0:
        raise ValueError('Invalid stopId format')
    return value

def validate_coordinates(value):
    if not isinstance(value, float) or value < -90 or value > 90:
        raise ValueError('Invalid coordinates format')
    return value

def validate_address(address):
    pattern = r'^[\w\s\d.,\-/"]+$'
    if not re.match(pattern, address):
        raise ValueError('Invalid address format')
    return address