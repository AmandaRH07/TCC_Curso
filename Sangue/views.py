from django.shortcuts import render
from .forms import TipoSanguineoForm

from CadastroDePessoa.models import Usuario

def sangue(request):
    usuario = Usuario.objects.get(id_fk_cadastro_user=request.user.id)
    form = TipoSanguineoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

    return render(request, "sangue.html", {"form": form, 'dados_user': usuario})
