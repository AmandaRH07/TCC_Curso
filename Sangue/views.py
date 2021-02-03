from django.shortcuts import render
from .forms import TipoSanguineoForm

def sangue(request):
    form = TipoSanguineoForm(request.POST or None)
    if request.method=='POST':
        print("entrou")
        tipo_sanguineo = request.POST.get('tipo_sanguineo')

    return render(request, "sangue.html", {"form": form})
