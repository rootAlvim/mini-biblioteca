from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Livro


def listar_livros(request):
    livros = Livro.objects.all()

    return render(request, 'lista_livro.html', {'livros': livros})