from django.shortcuts import render
from .forms import VacinasForm

from CadastroDePessoa.models import Usuario

def vacinas(request):
    usuario = Usuario.objects.get(id_fk_cadastro_user=request.user.id)
    form = VacinasForm(request.POST or None)
    if str(request.method) == 'POST' or str(request.method) == 'FILES':
        if form.is_valid():
            print("oi")
            form.save()
    return render(request, "vacinas.html", {"form": form, 'dados_user': usuario})