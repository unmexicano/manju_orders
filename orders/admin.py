from django.contrib import admin
from .models import manjus, categoria, UserOrder, SavedCarts
from tinymce.widgets import TinyMCE
from django.db import models

class categoriaAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.TextField: {'widget': TinyMCE()},
            }

class manjusdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.TextField: {'widget': TinyMCE()},
            }


admin.site.register(categoria,CategoryAdmin)
admin.site.register(manjus, manjusAdmin)
admin.site.register(UserOrder)
admin.site.register(SavedCarts)
