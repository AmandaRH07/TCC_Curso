from django.shortcuts import render
from .forms import HistoricoConsultasForm
from django.http import HttpResponseRedirect
from CadastroDePessoa.models import Usuario
from .models import HistoricoConsultas

from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='index_login')
def historico_consultas(request):
    usuario = Usuario.objects.get(id_fk_cadastro_user=request.user)
    dados_historico = HistoricoConsultas.objects.filter(fk_usuario_historico_consulta=usuario.id_usuario)

    if str(request.method) == 'POST' or str(request.method) == 'FILES':
        form = HistoricoConsultasForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("historico")

    return render(request, "historico.html", {'dados_user': usuario, 'dados_historico': dados_historico})
