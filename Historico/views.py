from django.shortcuts import render
from .forms import HistoricoConsultasForm

from CadastroDePessoa.models import Usuario


def historico_consultas(request):
    usuario = Usuario.objects.get(id_fk_cadastro_user=request.user)
    form = HistoricoConsultasForm(request.POST, request.FILES or None)
    if str(request.method) == 'POST' or str(request.method) == 'FILES':
        if form.is_valid():
            form.save()
        else: 
            print("invalido")
            print(form)

    return render(request, "historico.html", {"form": form, 'dados_user': usuario})