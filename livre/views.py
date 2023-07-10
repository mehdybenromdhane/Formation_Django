from django.shortcuts import render
from .models import Livre

# Create your views here.


def list(req):
    livres = Livre.objects.all()

    return render(req, 'livre.html', {'livre': livres})
