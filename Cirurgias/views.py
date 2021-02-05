from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .forms import CirurgiasForm
from .models import Cirurgias
from CadastroDePessoa.models import Usuario

from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='index_login')
def cirurgia(request):
    usuario = Usuario.objects.get(id_fk_cadastro_user=request.user.id)
    dados_cirurgias = Cirurgias.objects.filter(fk_usuario_cirurgias=usuario.id_usuario)

    if str(request.method) == 'POST':
        form = CirurgiasForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("cirurgias")
    return render(request, "cirurgias.html", {'dados_user': usuario, 'dados_cirurgias': dados_cirurgias})
