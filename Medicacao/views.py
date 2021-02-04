from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from CadastroDePessoa.models import Usuario

from .forms import MedicacaoForm

@login_required(redirect_field_name='index_login')
def medicacao(request):
    usuario = Usuario.objects.get(id_fk_cadastro_user=request.user)
    form = MedicacaoForm(request.POST, request.FILES or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()
        
    return render(request, "medicacao.html", {"usuario": usuario})