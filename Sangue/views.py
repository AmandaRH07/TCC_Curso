from django.shortcuts import render
from .forms import TipoSanguineoForm

def sangue(request):
    form = TipoSanguineoForm(request.POST or None)
    return render(request, "sangue.html", {"form": form})
