from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')

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
