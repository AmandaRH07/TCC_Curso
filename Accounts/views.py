from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User


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

    nome = request.POST.get('nome')
    nascimento = request.POST.get('nascimento')
    sexo = request.POST.get('sexo')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    telefone = request.POST.get('telefone')
    senha = request.POST.get('senha')
    
    user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome, last_name=nome)
    user.save()

    return redirect('index_login')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
