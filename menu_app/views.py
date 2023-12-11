from django.shortcuts import render
from menu_app.models import Menu
from django.views.generic import ListView


class MenuListView(ListView):
    model = Menu
    template_name = 'menu_app/menu_list.html'
    context_object_name = 'items'


def draw_menu(request, name):
    return render(request, 'menu_app/menu.html', {'name': name})
