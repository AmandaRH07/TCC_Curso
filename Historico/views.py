from django.shortcuts import render
from .forms import HistoricoConsultasForm
from django.http import HttpResponseRedirect
from CadastroDePessoa.models import Usuario
from .models import HistoricoConsultas


def historico_consultas(request):
    usuario = Usuario.objects.get(id_fk_cadastro_user=request.user)
    form = HistoricoConsultasForm(request.POST, request.FILES or None)
    dados_historico = HistoricoConsultas.objects.filter(fk_usuario_historico_consulta=usuario.id_usuario)

    if str(request.method) == 'POST' or str(request.method) == 'FILES':
        form = HistoricoConsultasForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("historico")
        else: 
            print("invalido")
            print(form)

    return render(request, "historico.html", {"form": form, 'dados_user': usuario, 'dados_historico': dados_historico})
