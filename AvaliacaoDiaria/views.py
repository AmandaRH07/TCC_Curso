from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import AvaliacaoDiariaForm

from CadastroDePessoa.models import Usuario


@login_required(redirect_field_name='index_login')
def index(request):
    usuario = Usuario.objects.get(id_fk_cadastro_user=request.user)
    form = AvaliacaoDiariaForm(request.POST or None)
    if str(request.method) == 'POST' :
        if form.is_valid():
            form.save()
        else:
            print("form invalid")
    return render(request, "index.html", {"form": form, 'dados_user': usuario})

