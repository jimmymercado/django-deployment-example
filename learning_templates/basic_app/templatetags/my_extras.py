from django import template

register = template.Library()

@register.filter(name='cut')
def cut_func(val, arg):
    """
    This cuts out all values of 'arg' from the string!
    """
    return val.repr(arg, '')

#register.filter('cut', cut_func)

