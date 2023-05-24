from django.contrib import admin
from .models import Fornecedor, Marca, Produto

# Register your models here.
admin.site.register(Fornecedor)
admin.site.register(Marca)
admin.site.register(Produto)
