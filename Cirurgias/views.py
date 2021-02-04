from django.shortcuts import render
from .forms import CirurgiasForm

from CadastroDePessoa.models import Usuario

def cirurgia(request):
    usuario = Usuario.objects.get(id_fk_cadastro_user=request.user.id)
    form = CirurgiasForm(request.POST or None)
    if str(request.method) == 'POST' or str(request.method) == 'FILES':
        if form.is_valid():
            form.save()
    return render(request, "cirurgias.html", {"form": form, 'dados_user': usuario})