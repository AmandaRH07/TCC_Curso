from django.shortcuts import render, redirect, get_object_or_404
from .forms import TipoSanguineoForm
 
from CadastroDePessoa.models import Usuario
from Sangue.models import TipoSanguineo
 
 
from django.contrib.auth.decorators import login_required
 
@login_required(redirect_field_name='index_login')
def sangue(request):
    # usuario = Usuario.objects.get(id_fk_cadastro_user=request.user.id)
    usuario = get_object_or_404(Usuario, id_fk_cadastro_user=request.user.id)
    tipo_sanguineo = TipoSanguineo.objects.filter(fk_usuario_tipo_sanguineo=usuario.id_usuario)
 
    form = TipoSanguineoForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('sangue')
 
    return render(request, "sangue.html", {'dados_user': usuario, 'tipo_sanguineo': tipo_sanguineo})
 

@login_required(redirect_field_name='index_login')
def sangue_detail(request):
    usuario = get_object_or_404(Usuario, id_fk_cadastro_user=request.user)
 
    tipo_sanguineo = TipoSanguineo.objects.filter(fk_usuario_tipo_sanguineo=usuario.id_usuario)
 
    if str(request.method) == 'POST':
        form = TipoSanguineoForm(request.POST, instance=tipo_sanguineo[0])
        if form.is_valid():
            form.save()
            return redirect('sangue')
 
    return render(request, "sangue.html", {'dados_user': usuario, 'tipo_sanguineo': tipo_sanguineo})
