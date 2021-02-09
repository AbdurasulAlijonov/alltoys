from django import template

register = template.Library()

@register.inclusion_tag('toys/employees.html')
def render_employee_list(employees):
    return {'employees':employees}