from django.contrib import admin
from .models import Category
# Register your models here.

class CagtegoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('Category_name',)}
    list_display = ['Category_name', 'slug']


admin.site.register(Category, CagtegoryAdmin)
