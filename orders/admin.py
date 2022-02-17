from django.contrib import admin
from .models import opciones, Category, UserOrder, SavedCarts
from tinymce.widgets import TinyMCE
from django.db import models


class categoriaAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

class opcionesAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)




admin.site.register(Category, categoriaAdmin)
admin.site.register(opciones, opcionesAdmin)
admin.site.register(UserOrder)
admin.site.register(SavedCarts)
