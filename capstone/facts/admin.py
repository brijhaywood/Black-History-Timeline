from django.contrib import admin
from .models import Facts

# Register your models here.
class FactsAdmin(admin.ModelAdmin):
    list = ('title', 'year', 'description', 'category')

admin.site.register(Facts, FactsAdmin)