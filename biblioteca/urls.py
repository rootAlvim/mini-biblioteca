from django.urls import path
from .views import listar_livros, autor

urlpatterns = [
    path('livros/', listar_livros, name='listar_livros'),
    path('livros/autor/<int:id>/', autor, name='autor'),
]