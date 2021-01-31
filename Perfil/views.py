from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from CadastroDePessoa.forms import UsuarioForm
from CadastroDePessoa.models import Usuario

@login_required(redirect_field_name='index_login')
def perfil(request):

    form = UsuarioForm(request.POST, request.FILES or None)

    if str(request.method) == 'POST' or str(request.method) == 'FILES':
        print(form)
        if form.is_valid():
            print('form valid')

            user_id = request.POST.get("id_user")
            nome = request.POST.get("nome")
            email = request.POST.get('email')
            usuario = request.POST.get('usuario')
            foto = request.FILES.get('foto')
            print(foto)
            nascimento = request.POST.get('nascimento')
            sexo =  request.POST.get('sexo')
            telefone = request.POST.get('telefone')

            user = Usuario.objects.get(id_fk_cadastro_user=user_id)
    
            user.nome = nome
            user.email = email
            user.usuario = usuario
            if foto:
                user.foto = foto
            user.sexo = sexo
            user.telefone = telefone
            user.save()
    else:
        print('form invalid')

    return render(request, "perfil.html", {'dados_user': Usuario.objects.get(id_fk_cadastro_user=request.user.id)})