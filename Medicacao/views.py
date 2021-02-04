from django.shortcuts import render
from .forms import EntryCreationForm

def medicacao(request):
    form = EntryCreationForm(request.POST or None)
    return render(request, "medicacao.html", {"form":form})

