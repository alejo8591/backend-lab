from django.shortcuts import render

def index(request):
    context_dict = {'message':'Mis Peliculas'}
    return render(request, 'index.html', context_dict)

def uploads(request):
    context_dict = {'message':'Archivos subidos'}
    return render(request, 'uploads.html', context_dict)
