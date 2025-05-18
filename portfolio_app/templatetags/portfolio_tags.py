from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """数値を掛け算するフィルター"""
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        return '' 