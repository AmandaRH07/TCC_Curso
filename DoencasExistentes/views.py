from django.shortcuts import render

from .forms import DoencasExistentesForm

# Create your views here.
def doencas_existentes(request):
    form = DoencasExistentesForm(request.POST, request.FILES or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()
    return render(request, "doencas-existentes.html", {"form": form})