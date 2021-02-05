from django.shortcuts import render, redirect

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages

from CadastroDePessoa.forms import UsuarioForm
from CadastroDePessoa.models import Usuario

from django.contrib.auth.decorators import login_required

def login(request):
    if request.method !="POST":
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        return redirect('index')

def logout(request):
    auth.logout(request)
    return redirect('index_login')

def cadastro(request):
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')

    form = UsuarioForm(request.POST or None)

    nome = request.POST.get("nome")
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    foto = request.FILES.get('foto')
    nascimento = request.POST.get('nascimento')
    sexo =  request.POST.get('sexo')
    telefone = request.POST.get('telefone')
    

    if form.is_valid():
        user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome, last_name=nome)
        user.save()
        usuario_db = Usuario(nome=nome, foto=foto, nascimento=nascimento, sexo=sexo, telefone=telefone, email=email, id_fk_cadastro_user=user)
        usuario_db.save()
    else:
        print('form invalid')

    return redirect('index_login')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
