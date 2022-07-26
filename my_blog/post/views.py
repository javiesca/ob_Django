import email
from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Entry

# Create your views here.
def queries(request):

    #Obtener todos los elementos
    authors = Author.objects.all()

    #Obtener autores según filtro
    filtered = Author.objects.filter(email = "sally63@example.org")

    #Obtener un único objeto(filtrado)
    author = Author.objects.get(id=1)

    #Limitar resultados de una consulta. (10 primeros)
    limits = Author.objects.all()[:10]

    #Saltando los elementos que queramos (10 elementos saltando los 5 primeros)
    offsets = Author.objects.all()[5:15]
                                                #CONTESTO
    return render(request, 'post/queries.html', {'authors':authors, 'filtered':filtered, 'author':author, 'limits':limits, 'offsets':offsets})
