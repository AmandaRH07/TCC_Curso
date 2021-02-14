from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from CadastroDePessoa.models import Usuario

from .forms import AvaliacaoDiariaForm
from .models import AvaliacaoDiaria


@login_required(redirect_field_name='index_login')
def index(request):
    usuario = get_object_or_404(Usuario, id_fk_cadastro_user=request.user)

    dados_avaliacao_diaria = AvaliacaoDiaria.objects.filter(
        fk_usuario_avaliacao_diaria=usuario.id_usuario).order_by('-data')
    
    if str(request.method) == 'POST' :
        form = AvaliacaoDiariaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, "index.html", 
        {
            'dados_user': usuario,
            'dados_avaliacao_diaria': dados_avaliacao_diaria
        })

