from django.contrib import admin
from .models import User, Product, Batch

models = [User, Product, Batch]

[admin.site.register(model) for model in models]