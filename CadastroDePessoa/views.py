from django.shortcuts import render, redirect
from .forms import UsuarioForm
from .models import Usuario

# Create your views here.
# def cadastro_pessoa(request):
#     form = UsuarioForm(request.POST or None)

#     if str(request.method) == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('perfil')

#     return render(request, 'cadastro-pessoa.html')
