from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from CadastroDePessoa.forms import UsuarioUpdateForm
from CadastroDePessoa.models import Usuario

@login_required(redirect_field_name='index_login')
def perfil(request):
    user = Usuario.objects.get(id_fk_cadastro_user=request.user)
    form = UsuarioUpdateForm(request.POST, request.FILES or None, instance=user)

    if str(request.method) == 'POST' or str(request.method) == 'FILES':
        if form.is_valid():
            form.save()
    
    return render(request, "perfil.html", {'dados_user': Usuario.objects.get(id_fk_cadastro_user=request.user.id), 'form': form})
