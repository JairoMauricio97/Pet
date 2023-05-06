from django.shortcuts import render
from pet.models import Perrito

# Create your views here.
def Blog(request):
    perritos = Perrito.objects.all()
    context = {
    'perritos': perritos
    }
    return render(request, 'Blog.html', context)

def perritoDetalle(request,pk):
    perrito = Perrito.objects.get(pk=pk)
    context = {
    'perrito': perrito
    }
    return render(request, 'perritoDetalle.html', context)