from django.contrib import admin
from .models import *
# Register your models here.
class EditInline(admin.TabularInline):
    model = Livro
    extra = 0

@admin.register(Autor)
class Autoradmin(admin.ModelAdmin):
    inlines = [EditInline]

@admin.register(Categoria)
class Categoriaadmin(admin.ModelAdmin):
    ...

@admin.register(Livro)
class Livroadmin(admin.ModelAdmin):
    list_display = ['titulo','autor','ano_publicacao','disponivel']
    search_fields = ['titulo','autor__nome']
    list_filter = ['disponivel','categorias__nome']
    