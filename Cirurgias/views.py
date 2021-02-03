from django.shortcuts import render
from .forms import CirurgiasForm

def cirurgia(request):
    form = CirurgiasForm(request.POST or None)
    if str(request.method) == 'POST' or str(request.method) == 'FILES':
        if form.is_valid():
            form.save()
    return render(request, "cirurgias.html", {"form": form})