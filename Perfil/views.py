from django.shortcuts import render


def editar_perfil(request):
    return render(request, "editar-perfil.html")