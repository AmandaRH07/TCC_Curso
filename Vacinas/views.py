from django.shortcuts import render

def vacinas(request):
    return render(request, "vacinas.html")
