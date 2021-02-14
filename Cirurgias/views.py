from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import CirurgiasForm
from .models import Cirurgias

from CadastroDePessoa.models import Usuario



@login_required(redirect_field_name='index_login')
def cirurgia(request):
    usuario = get_object_or_404(Usuario, id_fk_cadastro_user=request.user)
    dados_cirurgias = Cirurgias.objects.filter(fk_usuario_cirurgias=usuario.id_usuario)

    if str(request.method) == 'POST':
        form = CirurgiasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cirurgias')
            
    return render(request, "cirurgias.html",
        {
        'dados_user': usuario,
        'dados_cirurgias': dados_cirurgias
        })


@login_required(redirect_field_name='index_login')
def cirurgia_detail(request, pk):
    usuario = get_object_or_404(Usuario, id_fk_cadastro_user=request.user)
    dados_cirurgias = Cirurgias.objects.filter(fk_usuario_cirurgias=usuario.id_usuario)

    cirurgia_detail = get_object_or_404(Cirurgias, id_cirugias=pk)

    if str(request.method) == 'POST':
        form = CirurgiasForm(request.POST, instance=cirurgia_detail)
        if form.is_valid():
            form.save()
            return redirect('cirurgias')

    return render(request, "cirurgias.html",
        {
            "dados_user": usuario,
            'dados_cirurgias': dados_cirurgias,
            'cirurgia_detail': cirurgia_detail
        })


@login_required(redirect_field_name='index_login')
def cirurgia_delete(request, pk):
    cirurgia_detail = get_object_or_404(Cirurgias, id_cirugias=pk)
    cirurgia_detail.delete()

    return redirect('cirurgias')

