from django.shortcuts import render
from .forms import HistoricoConsultasForm

def historico_consultas(request):
    form = HistoricoConsultasForm(request.POST, request.FILES or None)
    if str(request.method) == 'POST' or str(request.method) == 'FILES':
        if form.is_valid():
            form.save()

    return render(request, "historico.html", {"form": form})
