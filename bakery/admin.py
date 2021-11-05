from django.contrib import admin
from .models import ingredients,product,recipe
# Register your models here.
admin.site.register(ingredients)
admin.site.register(product)
admin.site.register(recipe)