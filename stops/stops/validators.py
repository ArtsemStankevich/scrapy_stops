import re
from pydantic import ValidationError, validator

# Validator functions
def validate_fields(value):
    if not value:
        raise ValueError('Field cannot be empty')
    return value

def validate_coordinates(cls, value):
    if value < -90 or value > 90:
        raise ValueError('Invalid latitude or longitude value')
    return value