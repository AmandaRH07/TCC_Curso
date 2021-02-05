from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import MedicacaoForm
from .models import Medicamentos

from CadastroDePessoa.models import Usuario



@login_required(redirect_field_name='index_login')
def medicacao(request):
    usuario = Usuario.objects.get(id_fk_cadastro_user=request.user)
    dados_medicamentos = Medicamentos.objects.filter(fk_user_medicacao=usuario.id_usuario)

    if str(request.method) == 'POST':
        form = MedicacaoForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("medicacao")
            
    return render(request, "medicacao.html", {"usuario": usuario, 'dados_medicamentos': dados_medicamentos})