import re
from pydantic import ValidationError, validator

def validate_text_fields(value):
    if value is None:
        return value
    pattern = r'^[\w\s\dąćęłńóśźżĄĆĘŁŃÓŚŹŻ\-,.()/\'"]+(\s\(N\\Ż\))?$'
    if not re.match(pattern, value):
        raise ValueError('Invalid text format')
    return value

def validate_fields(value):
    if not value:
        raise ValueError('Field cannot be empty')
    return value

def validate_opening_hours(value):
    pattern = r'^\d{2}:\d{2}-\d{2}:\d{2}$'
    if not re.match(pattern, value):
        raise ValueError('Invalid opening hours format. Use HH:MM-HH:MM')
    return value

def validate_id(value):
    if not isinstance(value, int) or value < 0:
        raise ValueError('Invalid stopId format')
    return value

def validate_city(city):
    pattern = r'^[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ\s]+$'
    if not re.match(pattern, city):
        raise ValueError('Invalid city format')
    return city


def validate_coordinates(value):
    if not isinstance(value, float) or value < -90 or value > 90:
        raise ValueError('Invalid coordinates format')
    return value

def validate_address(address):
    pattern = r'^[\w\s\d.,\-/"]+$'
    if not re.match(pattern, address):
        raise ValueError('Invalid address format')
    return address