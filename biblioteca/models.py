from django.db import models

# Create your models here.
from django.db import models
class Autor(models.Model):
    nome = models.CharField(max_length=60,null=False,blank=False)
    nacionalidade = models.CharField(max_length=60, null=True, blank=True)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = 'Autores'
        ordering = ['nome']



class Categoria(models.Model):
    nome = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor,related_name='livros',on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria,blank=True)

    ano_publicacao = models.IntegerField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return (f"{self.titulo}")