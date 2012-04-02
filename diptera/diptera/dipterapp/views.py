# Create your views here.
from django.http import HttpResponse
from models import *

def testview(request):
    article = Article(title = 'titulo ejemplo',
    content = 'test content')
    article.save()

    return HttpResponse("<h1>Listo Salvado!</h1>")
