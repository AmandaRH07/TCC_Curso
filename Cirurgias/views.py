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

@login_required(redirect_field_name='index_login')
def cirurgia_detail(request, pk):
    usuario = Usuario.objects.get(id_fk_cadastro_user=request.user)
    dados_cirurgias = Cirurgias.objects.filter(fk_usuario_cirurgias=usuario.id_usuario)

    cirurgia_detail = Cirurgias.objects.get(id_cirugias=pk)

    if str(request.method) == 'POST':
        form = CirurgiasForm(request.POST, instance=cirurgia_detail)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('cirurgias')

    return render(request, "cirurgias.html", {"usuario": usuario, 'dados_cirurgias': dados_cirurgias, 'cirurgia_detail': cirurgia_detail})


@login_required(redirect_field_name='index_login')
def cirurgia_delete(request, pk):
    cirurgia = Cirurgias.objects.get(id_cirugias=pk)
    cirurgia.delete()

    return redirect('cirurgias')

