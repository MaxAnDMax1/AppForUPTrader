from django.contrib import admin
from menu_app.models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'name_url', 'parent')
    list_filter = ('name',)
    search_fields = ('name', 'url', 'name_url')
    ordering = ('name', 'id')


admin.site.register(Menu, MenuAdmin)
