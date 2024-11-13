from django import template
from decimal import Decimal, InvalidOperation

register = template.Library()

@register.filter
def get_attr(obj, attr_name):
    """Get attribute from an object by name."""
    return getattr(obj, attr_name, None)

@register.filter
def index(sequence, i):
    """Get an item at the specified index in a list or tuple."""
    try:
        return sequence[i]
    except (IndexError, TypeError):
        return None

@register.filter
def to_float(value):
    """Convert a value to a float."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return value

@register.filter
def to_decimal(value):
    """Convert a value to Decimal for currency formatting."""
    try:
        return Decimal(value)
    except (InvalidOperation, ValueError, TypeError):
        return value

@register.filter
def format_currency(value, symbol="$"):
    """Format a value as currency, using a specified currency symbol."""
    try:
        # Convert to Decimal for accuracy
        value = to_decimal(value)
        return f"{symbol}{value:,.2f}"  # Example format: $1,234.56
    except (InvalidOperation, ValueError, TypeError):
        return value  # Return as-is if conversion fails

@register.filter
def get_item(dictionary, key):
    """Retrieve a value from a dictionary by key."""
    if isinstance(dictionary, dict):
        return dictionary.get(key, None)
    return None

@register.filter
def get_attr(obj, attr):
    return getattr(obj, attr, None)
