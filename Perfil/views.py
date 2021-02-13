from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from AvaliacaoDiaria.models import AvaliacaoDiaria
from Cirurgias.models import Cirurgias
from DoencasExistentes.models import DoencasExistentes 
from Historico.models import HistoricoConsultas, HistoricoFamiliar 
from Medicacao.models import Medicamentos
from Sangue.models import TipoSanguineo
from Vacinas.models import Vacinas

from CadastroDePessoa.forms import UsuarioUpdateForm
from CadastroDePessoa.models import Usuario

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
# from django.views import View

import qrcode
import image

from xhtml2pdf import pisa
import requests
import json

@login_required(redirect_field_name='index_login')
def perfil(request):
    # user = Usuario.objects.get(id_fk_cadastro_user=request.user)
    user = get_object_or_404(Usuario, id_fk_cadastro_user=request.user)

    form = UsuarioUpdateForm(request.POST, request.FILES or None, instance=user)

    if str(request.method) == 'POST' or str(request.method) == 'FILES':
        if form.is_valid():
            form.save()
    
    return render(request, "perfil.html", {'dados_user': Usuario.objects.get(id_fk_cadastro_user=request.user.id), 'form': form})

def informacoes(request):
    usuario = Usuario.objects.get(id_fk_cadastro_user=request.user).__dict__
    cirurgias = Cirurgias.objects.filter(fk_usuario_cirurgias=usuario['id_usuario'])
    doencas_existentes = DoencasExistentes.objects.filter(fk_usuario_doencas_existentes=usuario['id_usuario'])
    historico_consultas = HistoricoConsultas.objects.filter(fk_usuario_historico_consulta=usuario['id_usuario'])
    historico_familiar = HistoricoFamiliar.objects.filter(fk_usuario_historico_familiar=usuario['id_usuario'])
    medicamentos = Medicamentos.objects.filter(fk_user_medicacao=usuario['id_usuario'])
    sangue = TipoSanguineo.objects.filter(fk_usuario_tipo_sanguineo=usuario['id_usuario'])
    vacinas = Vacinas.objects.filter(fk_usuario_vacinas=usuario['id_usuario'])

    data = {
        'usuario': usuario,
        'cirurgias': cirurgias,
        'doencas_existentes': doencas_existentes,
        'historico_consultas': historico_consultas,
        'historico_familiar': historico_familiar,
        'medicamentos': medicamentos,
        'sangue': sangue,
        'vacinas': vacinas,
    }
    return render(request, "informacoes.html", data)


def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result, encoding='UTF-8')
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


# Opens up page as PDF
def pdf_view(request, hash_user):
    usuario = Usuario.objects.get(hash_user=hash_user).__dict__
    cirurgias = Cirurgias.objects.filter(fk_usuario_cirurgias=usuario['id_usuario'])
    doencas_existentes = DoencasExistentes.objects.filter(fk_usuario_doencas_existentes=usuario['id_usuario'])
    historico_consultas = HistoricoConsultas.objects.filter(fk_usuario_historico_consulta=usuario['id_usuario'])
    historico_familiar = HistoricoFamiliar.objects.filter(fk_usuario_historico_familiar=usuario['id_usuario'])
    medicamentos = Medicamentos.objects.filter(fk_user_medicacao=usuario['id_usuario'])
    sangue = TipoSanguineo.objects.filter(fk_usuario_tipo_sanguineo=usuario['id_usuario'])
    vacinas = Vacinas.objects.filter(fk_usuario_vacinas=usuario['id_usuario'])

    data = {
        'usuario': usuario,
        'cirurgias': cirurgias,
        'doencas_existentes': doencas_existentes,
        'historico_consultas': historico_consultas,
        'historico_familiar': historico_familiar,
        'medicamentos': medicamentos,
        'sangue': sangue,
        'vacinas': vacinas,
    }

    print(data)


    pdf = render_to_pdf('informacoes.html', data)

    return HttpResponse(pdf, content_type='application/pdf')


# #Automaticly downloads to PDF file
def pdf_download(request):
	
	pdf = render_to_pdf('app/informacoes.html', user)
	response = HttpResponse(pdf, content_type='application/pdf')
	filename = "Invoice_%s.pdf" %("12341231")
	content = "attachment; filename='%s'" %(filename)
	response['Content-Disposition'] = content
	return response


def qrcode (request):
    import qrcode

    usuario = Usuario.objects.get(id_fk_cadastro_user=request.user)

    qr = qrcode.QRCode(
        version=1,
        box_size=15,
        border=5
    )


    data = f'http://medfile1.herokuapp.com/pdf_view/{usuario.hash_user}/'
    print(data)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#112F41", back_color="#b0fffc")
    img.save(f'media/qrcode/{request.user.username}{usuario.id_usuario}.png')
    usuario.qrcode = f'qrcode/{request.user.username}{usuario.id_usuario}.png'
    usuario.save()
 
    return redirect('perfil')