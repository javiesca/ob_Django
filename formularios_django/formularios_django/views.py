from django.http import HttpResponse
from django.shortcuts import render
from .forms import CommentForm

def form(request):
    comment_form = CommentForm({'name':'Javi', 'url':'https://open-bootcamp.com', 'content': 'Comentatio', 'date':'13/05/1982'})
    return render(request, 'form.html', {'comment_form': comment_form})


def goal(request):
    if request.method != 'POST':
        return HttpResponse("El metodo GET no está permitido en esta ruta", 404)
    
    return HttpResponse(request.POST['name'])