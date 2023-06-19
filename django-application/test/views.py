from django.shortcuts import render

from .models import Name



# Create your views here.

def index(request):
    names = Name.objects.all()
    context = {
        'names': names,
    }
    return render(request, 'test/index.html', context)
