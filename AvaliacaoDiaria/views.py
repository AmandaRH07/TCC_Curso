from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='index_login')
def index(request):
    return render(request, "index.html")
