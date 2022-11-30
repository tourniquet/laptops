from django.contrib import admin

from .models import Brand, Model, Laptop

admin.site.register(Brand)
admin.site.register(Model)

class LaptopAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_filter = ('model', 'status',)

admin.site.register(Laptop, LaptopAdmin)
