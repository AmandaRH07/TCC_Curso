from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from CadastroDePessoa.models import Usuario

from .forms import HistoricoConsultasForm, HistoricoFamiliarForm, DoencaCronicaForm
from .models import HistoricoConsultas, HistoricoFamiliar, DoencaCronica


@login_required(redirect_field_name='index_login')
def historico_consultas(request):
    print("teste")
    usuario = get_object_or_404(Usuario, id_fk_cadastro_user=request.user)

    dados_historico = HistoricoConsultas.objects.filter(
        fk_usuario_historico_consulta=usuario.id_usuario)

    doenca_cronica = DoencaCronica.objects.filter(
        fk_usuario_doenca_cronica=usuario.id_usuario)
    if doenca_cronica:
        doenca_cronica = doenca_cronica[0]

    dados_familiar = HistoricoFamiliar.objects.filter(
        fk_usuario_historico_familiar=usuario.id_usuario)

    if str(request.method) == 'POST' or str(request.method) == 'FILES':
        form = HistoricoConsultasForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('historico')

    return render(request, "historico.html", 
    {
        'dados_user': usuario, 
        'dados_historico': dados_historico, 
        'dados_familiar': dados_familiar, 
        'doenca_cronica': doenca_cronica
    })


@login_required(redirect_field_name='index_login')
def historico_consultas_detail(request, pk):
    usuario = get_object_or_404(Usuario, id_fk_cadastro_user=request.user)

    dados_historico = HistoricoConsultas.objects.filter(
        fk_usuario_historico_consulta=usuario.id_usuario)
    dados_familiar = HistoricoFamiliar.objects.filter(
        fk_usuario_historico_familiar=usuario.id_usuario)

    historico_consultas_detail = get_object_or_404(
        HistoricoConsultas, id_historico_consultas=pk)

    if str(request.method) == 'POST' or str(request.method) == 'FILES':
        form = HistoricoConsultasForm(request.POST, request.FILES, instance=historico_consultas_detail)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('historico')

    return render(request, "historico.html",
        {
            'dados_user': usuario,
            'dados_historico': dados_historico,
            'dados_familiar': dados_familiar, 
            'historico_consultas_detail': historico_consultas_detail
        })
    

@login_required(redirect_field_name='index_login')
def historico_consultas_delete(request, pk):
    consulta = get_object_or_404(HistoricoConsultas, id_historico_consultas=pk)
    consulta.delete()

    return redirect('historico')


####################### HISTÓRICO FAMILIAR #######################
@login_required(redirect_field_name='index_login')
def historico_familiar(request):
    usuario = get_object_or_404(Usuario, id_fk_cadastro_user=request.user)

    dados_familiar = HistoricoFamiliar.objects.filter(
        fk_usuario_historico_familiar=usuario.id_usuario)

    if str(request.method) == 'POST':
        form = HistoricoFamiliarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('historico')

    return redirect('historico')


@login_required(redirect_field_name='index_login')
def historico_familiar_detail(request, pk):
    usuario = get_object_or_404(Usuario, id_fk_cadastro_user=request.user)

    dados_historico = HistoricoConsultas.objects.filter(
        fk_usuario_historico_consulta=usuario.id_usuario)
    dados_familiar = HistoricoFamiliar.objects.filter(
        fk_usuario_historico_familiar=usuario.id_usuario)

    historico_familiar_detail = get_object_or_404(HistoricoFamiliar, id_historico_familiar=pk)

    if str(request.method) == 'POST':
        form = HistoricoFamiliarForm(request.POST, instance=historico_familiar_detail)
        if form.is_valid():
            form.save()
            return redirect('historico')

    return render(request, "historico.html", 
        {
            'dados_user': usuario, 
            'dados_historico': dados_historico, 
            'dados_familiar': dados_familiar, 
            'historico_familiar_detail': historico_familiar_detail,
        })


@login_required(redirect_field_name='index_login')
def historico_familiar_delete(request, pk):
    historico_familiar = get_object_or_404(HistoricoFamiliar, id_historico_familiar=pk)
    historico_familiar.delete()

    return redirect('historico')


@login_required(redirect_field_name='index_login')
def doenca_cronica_create(request):
    usuario = get_object_or_404(Usuario, id_fk_cadastro_user=request.user)
    if str(request.method) == 'POST':
        form = DoencaCronicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('historico')
    return redirect('historico')


@login_required(redirect_field_name='index_login')
def doenca_cronica_edit(request):
    usuario = get_object_or_404(Usuario, id_fk_cadastro_user=request.user)
    doenca_cronica = get_object_or_404(
        DoencaCronica, fk_usuario_doenca_cronica=usuario.id_usuario)

    if str(request.method) == 'POST':
        form = DoencaCronicaForm(request.POST, instance=doenca_cronica)
        if form.is_valid():
            form.save()
            return redirect('historico')
            
    return redirect('historico')