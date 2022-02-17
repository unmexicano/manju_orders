from django.contrib import admin
from .models import opciones, Category, UserOrder, SavedCarts
from tinymce.widgets import TinyMCE
from django.db import models

class categoriaAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.TextField: {'widget': TinyMCE()},
            }

class opcionesAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.TextField: {'widget': TinyMCE()},
            }


admin.site.register(Category, categoriaAdmin)
admin.site.register(opciones, opcionesAdmin)
admin.site.register(UserOrder)
admin.site.register(SavedCarts)
