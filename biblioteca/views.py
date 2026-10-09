from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_list_or_404
from .models import *


def listar_livros(request):
    livros = Livro.objects.all()

    return render(request, 'lista_livro.html', {'livros': livros})

def autor(request,id):
    livro = get_list_or_404(Livro,autor__id=id)
    autor = Autor.objects.get(id=id)

    return render(request, 'pagina_autor.html', {'livros':autor.livros.all(),'autor':autor})