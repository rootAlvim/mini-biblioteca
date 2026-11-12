from django.urls import path
from .views import *

urlpatterns = [
    path('livros/', listar_livros, name='listar_livros'),
    path('livros/novo/', livro_form, name='novo_livro'),
    path('livros/<int:livro_id>/editar/', livro_form, name='editar_livro'),
    path('livros/autor/<int:id>/', autor, name='autor'),
    path('autores/', autores, name='autores'),
    path('criar-autor/', criar_autor, name='criar-autor'),
]