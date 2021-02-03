from django.shortcuts import render
from .forms import VacinasForm

def vacinas(request):
    form = VacinasForm(request.POST or None)
    if str(request.method) == 'POST' or str(request.method) == 'FILES':
        if form.is_valid():
            print("oi")
            form.save()
    return render(request, "vacinas.html", {"form": form})