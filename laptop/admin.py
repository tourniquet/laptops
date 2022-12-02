from django.contrib import admin

admin.site.register(Brand)
from .models import Brand, Laptop

class LaptopAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_filter = ('brand', 'status',)

admin.site.register(Laptop, LaptopAdmin)
