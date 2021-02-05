from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import VacinasForm
from .models import Vacinas

from CadastroDePessoa.models import Usuario

from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='index_login')
def vacinas(request):
    usuario = Usuario.objects.get(id_fk_cadastro_user=request.user.id)
    dados_vacinas = Vacinas.objects.filter(fk_usuario_vacinas=usuario.id_usuario)

    if str(request.method) == 'POST':
        form = VacinasForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("vacinas")
            
    return render(request, "vacinas.html", {'dados_user': usuario, 'dados_vacinas': dados_vacinas})