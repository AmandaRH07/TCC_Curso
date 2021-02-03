from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import AvaliacaoDiariaForm


@login_required(redirect_field_name='index_login')
def index(request):
    form = AvaliacaoDiariaForm(request.POST or None)
    if str(request.method) == 'POST' :
        if form.is_valid():
            print("oi")
            form.save()
        else:
            print("form invalid")
            print(form)
    return render(request, "index.html", {"form": form})

