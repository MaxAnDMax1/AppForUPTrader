from django import template
from django.db.models import Q

from menu_app.models import Menu
from django.utils.safestring import mark_safe


register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu = Menu.objects.filter(Q(url=menu_name) or Q(name_url=menu_name)).select_related('parent')
    return mark_safe(_render_menu(menu))


def _render_menu(menu):
    html = '<ul>'
    for item in menu:
        html += '<li>'
        if item.url:
            html += f'<a href="{item.url}">{item.name}</a>'
        elif item.named_url:
            html += f'<a href="{item.name_url}">{item.name}</a>'
        else:
            html += item.name
        if item.child.exists():
            html += _render_menu(item.child.all())
        html += '</li>'
    html += '</ul>'

    return html
