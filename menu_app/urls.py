from django.urls import path
from menu_app.views import draw_menu, MenuListView

app_name = 'menu_app'

urlpatterns = [
    path('', MenuListView.as_view(), name='menu-list'),
    path('<str:name>/', draw_menu, name='draw_menu'),
]
