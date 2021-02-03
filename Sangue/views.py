from django.shortcuts import render
from .forms import TipoSanguineoForm

def sangue(request):
    form = TipoSanguineoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

    return render(request, "sangue.html", {"form": form})
