from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import render, get_list_or_404
from .models import *
from .forms import *

def listar_livros(request):
    livros = Livro.objects.all()

    return render(request, 'lista_livro.html', {'livros': livros})

def autor(request,id):
    livro = Livro.objects.filter(id=id)
    autor = Autor.objects.get(id=id)

    return render(request, 'pagina_autor.html', {'livros':autor.livros.all(),'autor':autor})

def autores(request):
    autores = Autor.objects.all()
    return render(request,'autores.html',{'autores':autores})

def criar_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            autor = Autor.objects.create(
                nome = form.cleaned_data['nome'],
                nacionalidade = form.cleaned_data['nacionalidade'],
            )
            return redirect('autor',id=autor.id)
    else:
        form = AutorForm()
    return render(request,'criar_autor.html',{'form':form})