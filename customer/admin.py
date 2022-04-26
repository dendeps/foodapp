from django.contrib import admin

# Register your models here.
from .models import MenuItem, Category, Order

admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(Order)