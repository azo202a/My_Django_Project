from django import template

register = template.Library()

@register.filter
def greeting(value):
    """
    هذا الفلتر يضيف كلمة "Hello " إلى بداية النص.
    """
    return "Hello " + value