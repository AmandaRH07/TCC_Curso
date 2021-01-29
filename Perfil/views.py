from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from CadastroDePessoa.forms import UsuarioForm
from CadastroDePessoa.models import Usuario

@login_required(redirect_field_name='index_login')
def perfil(request):

    form = UsuarioForm(request.POST or None)
    print(request.user.email)


    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()
            messages.info(request, 'Perfil atualizado com sucesso!')
        else:
            messages.info(request, 'Erro ao atualizar perfil :(')

    return render(request, "perfil.html", {'dados_user': Usuario.objects.get(id_fk_cadastro_user=request.user.id)})