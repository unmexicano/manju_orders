from django.contrib import admin
from .models import opciones, Category, UserOrder, SavedCarts
from tinymce import models as tinymce_models
from django.db import models


class categoriaAdmin(admin.ModelAdmin):
    formfield_overrides = {
                              tinymce_models.HTMLField()},


class opcionesAdmin(admin.ModelAdmin):
    formfield_overrides = {
                               tinymce_models.HTMLField()},



admin.site.register(Category, categoriaAdmin)
admin.site.register(opciones, opcionesAdmin)
admin.site.register(UserOrder)
admin.site.register(SavedCarts)
