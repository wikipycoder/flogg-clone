from django.contrib import admin
from .models import Product, Category, Brand, Detail


models = [Product, Category, Brand, Detail]

for model in models:
    admin.site.register(model)

