import sys

from django.shortcuts import get_object_or_404, render_to_response, render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

from .menu import Menu
from .data_db import DataDB
from data.models import Data_DB

menu = Menu()
data_db = DataDB()

def home(request, lang):
	general_data = data_db.general(lang)
	section_data = data_db.home(lang)
	tmp = Data_DB.objects.filter(section=1)
	section_data_db = get_correct_lang(tmp, lang)
	main_menu = menu.get_main_menu(section_data['gral_info']['section'], lang)
	footer_menu = menu.get_footer_menu(lang)
	return render_to_response('sections/home.html', locals())

def about_us(request, lang=0, tag=''):
	general_data = data_db.general(lang)
	section_data = data_db.about_us(lang)
	tmp = Data_DB.objects.filter(section=2)
	section_data_db = get_correct_lang(tmp, lang)
	main_menu = menu.get_main_menu(section_data['gral_info']['section'], lang)
	footer_menu = menu.get_footer_menu(lang)
	return render_to_response('sections/about_us.html', locals())

def insurance(request, lang=0, tag=''):
	general_data = data_db.general(lang)
	section_data = data_db.insurance(lang)
	tmp = Data_DB.objects.filter(section=3)
	section_data_db = get_correct_lang(tmp, lang)
	main_menu = menu.get_main_menu(section_data['gral_info']['section'], lang)
	footer_menu = menu.get_footer_menu(lang)
	return render_to_response('sections/insurance.html', locals())

def procedures(request, lang=0, tag=''):
	general_data = data_db.general(lang)
	section_data = data_db.procedures(lang)
	tmp = Data_DB.objects.filter(section=4)
	section_data_db = get_correct_lang(tmp, lang)
	main_menu = menu.get_main_menu(section_data['gral_info']['section'], lang)
	footer_menu = menu.get_footer_menu(lang)
	return render_to_response('sections/procedures.html', locals())

def permits(request, lang=0, tag=''):
	general_data = data_db.general(lang)
	section_data = data_db.permits(lang)
	tmp = Data_DB.objects.filter(section=5)
	section_data_db = get_correct_lang(tmp, lang)
	main_menu = menu.get_main_menu(section_data['gral_info']['section'], lang)
	footer_menu = menu.get_footer_menu(lang)
	return render_to_response('sections/permits.html', locals())

def audits(request, lang=0, tag=''):
	general_data = data_db.general(lang)
	section_data = data_db.audits(lang)
	tmp = Data_DB.objects.filter(section=6)
	section_data_db = get_correct_lang(tmp, lang)
	main_menu = menu.get_main_menu(section_data['gral_info']['section'], lang)
	footer_menu = menu.get_footer_menu(lang)
	return render_to_response('sections/audits.html', locals())

def buy_online(request, lang=0, tag=''):
	general_data = data_db.general(lang)
	section_data = data_db.buy_online(lang)
	tmp = Data_DB.objects.filter(section=7)
	section_data_db = get_correct_lang(tmp, lang)
	main_menu = menu.get_main_menu(section_data['gral_info']['section'], lang)
	footer_menu = menu.get_footer_menu(lang)
	return render_to_response('sections/buy_online.html', locals())

def contact(request, lang=0, tag=''):
	general_data = data_db.general(lang)
	section_data = data_db.contact(lang)
	tmp = Data_DB.objects.filter(section=8)
	section_data_db = get_correct_lang(tmp, lang)
	main_menu = menu.get_main_menu(section_data['gral_info']['section'], lang)
	footer_menu = menu.get_footer_menu(lang)
	return render_to_response('sections/contact.html', locals())

def get_correct_lang(data, lang):
	response = []
	for row in data:
		if lang == 0:
			response.append(row.text_sp)
		elif lang == 1:
			response.append(row.text_en)
	return response

@csrf_exempt
def send_mail_form(request):
	c = {}
	c.update(csrf(request))
	if request.is_ajax():
		response = 'error'
		email_msg = ''
		name = request.POST.get('name', '')
		email = request.POST.get('email', '')
		tel = request.POST.get('tel', '')
		service = request.POST.get('select_service', '')
		message = request.POST.get('message', '')
		if name == '' or email == '' or message == '':
			response = 'empty_data'
		else:
			email_msg = """
				Name: <b>""" + str(name)  + """</b><br/>
				Email: <b>""" + str(email)  + """</b><br />
				Tel: <b>""" + str(tel)  + """</b><br />
				Service: <b>""" + str(service)  + """</b><br />
				Message: <b>""" + str(message)  + """</b><br />
			"""
			try:
				text_content = 'Mensaje enviado desde la forma de contacto'
				html_content = email_msg
				msg = EmailMultiAlternatives('Contact Form', text_content, email, ['mario@serviciosgaritaotay.com', 'info.mintitmedia@gmail.com',])
				msg.attach_alternative(html_content, "text/html")
				msg.send()
				response = "success"
			except:
				response = "Unexpected error:", sys.exc_info()
		return HttpResponse(response, c)
	else:
		return HttpResponse(status=400)
