from django.shortcuts import render
from .forms import HistoricoConsultasForm, HistoricoFamiliarForm
from django.http import HttpResponseRedirect
from CadastroDePessoa.models import Usuario
from .models import HistoricoConsultas, HistoricoFamiliar

from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='index_login')
def historico_consultas(request):
    usuario = Usuario.objects.get(id_fk_cadastro_user=request.user)
    dados_historico = HistoricoConsultas.objects.filter(fk_usuario_historico_consulta=usuario.id_usuario)
    dados_familiar = HistoricoFamiliar.objects.filter(fk_usuario_historico_familiar=usuario.id_usuario)

    if str(request.method) == 'POST' or str(request.method) == 'FILES':
        form = HistoricoConsultasForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("historico")

    return render(request, "historico.html", {'dados_user': usuario, 'dados_historico': dados_historico, 'dados_familiar': dados_familiar})

@login_required(redirect_field_name='index_login')
def historico_familiar(request):
    print("entrou")
    usuario = Usuario.objects.get(id_fk_cadastro_user=request.user)
    dados_familiar = HistoricoFamiliar.objects.filter(fk_usuario_historico_familiar=usuario.id_usuario)

    if str(request.method) == 'POST':
        form = HistoricoFamiliarForm(request.POST)
        if form.is_valid():
            print("eh valido")
            form.save()
            return HttpResponseRedirect("historico")
        else:
            print("n eh valido")
            print(form)
    else:
        print("n eh post")

    return redirect('historico')