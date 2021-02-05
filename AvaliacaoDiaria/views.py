from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import AvaliacaoDiariaForm
from .models import AvaliacaoDiaria
from CadastroDePessoa.models import Usuario


@login_required(redirect_field_name='index_login')
def index(request):
    usuario = Usuario.objects.get(id_fk_cadastro_user=request.user)
    dados_avaliacao_diaria = AvaliacaoDiaria.objects.filter(fk_usuario_avaliacao_diaria=usuario.id_usuario)
    
    if str(request.method) == 'POST' :
        form = AvaliacaoDiariaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("avaliacao-diaria")

    return render(request, "index.html", {'dados_user': usuario, 'dados_avaliacao_diaria':dados_avaliacao_diaria})

