from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import MedicacaoForm
from .models import Medicamentos

from CadastroDePessoa.models import Usuario


@login_required(redirect_field_name='index_login')
def medicacao(request):
    usuario = get_object_or_404(Usuario, id_fk_cadastro_user=request.user)
    dados_medicamentos = Medicamentos.objects.filter(
        fk_user_medicacao=usuario.id_usuario)

    if str(request.method) == 'POST':
        form = MedicacaoForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('medicacao')
            
    return render(request, "medicacao.html",
        {
            "usuario": usuario,
            'dados_medicamentos': dados_medicamentos
        })


@login_required(redirect_field_name='index_login')
def medicacao_detail(request, pk):
    usuario = get_object_or_404(Usuario, id_fk_cadastro_user=request.user)
    dados_medicamentos = Medicamentos.objects.filter(
        fk_user_medicacao=usuario.id_usuario)

    medicacao_detail = get_object_or_404(Medicamentos, id_medicamentos=pk)

    if str(request.method) == 'POST':
        form = MedicacaoForm(request.POST, instance=medicacao_detail)
        if form.is_valid():
            form.save()
            return redirect('medicacao')

    return render(request, "medicacao.html", 
        {
            "usuario": usuario,
            'dados_medicamentos': dados_medicamentos,
            'medicacao_detail': medicacao_detail
        })


@login_required(redirect_field_name='index_login')
def medicacao_delete(request, pk):
    medicacao = get_object_or_404(Medicamentos, id_medicamentos=pk)
    medicacao.delete()

    return redirect('medicacao')
