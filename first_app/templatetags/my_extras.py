from django import template

register = template.Library()

@register.filter(name='cut_custom')
def cut_custom(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg, '')

# register.filter('cut', cut)