# -*- coding: utf-8 -*-
import re
import unidecode


class Menu(object):

	items = [
		[#ESPANISH			
			{								
				'title': 'Inicio',
				'href': 'inicio',
				'in_footer': '',
			},
			{				
				'title': 'Nosotros',
				'href': 'nosotros',
				'in_footer': '',
			},
			{				
				'title': 'Seguros',
				'href': 'seguros',
				'in_footer': '',
				'child':[
					{
						'title': 'E.U.',
						'href': 'eu',
					},
					{
						'title': 'Mx',
						'href': 'mx',
					},
				]
			},
			{				
				'title': 'Trámites y Permisos',
				'href': 'tramites-permisos',
				'in_footer': '',
				'child':[
					{
						'title': 'DMV',
						'href': 'dmv',
					},
					{
						'title': 'E.U.',
						'href': 'eu',
					},
					{
						'title': 'México',
						'href': 'mx',
					},
					{
						'title': 'Permisos',
						'href': '../permisos',
					},
				]
			},
			{				
				'title': 'Auditorias',
				'href': 'auditorias',
				'in_footer': '',
				#'child':[
					#{
						#'title': 'Servicios de consultoría en auditoría federales y estatales',
						#'href': 'servicios-consultoria-auditoria',
					#},
				#]
			},
			{				
				'title': 'Compra en Línea',
				'href': 'compra-linea',
				'in_footer': '',
			},
			{				
				'title': 'Contacto',
				'href': 'contacto',
				'in_footer': '',
			},
		],
		[#ENGLISH			
			{								
				'title': 'Home',
				'href': 'home',
				'in_footer': '',
			},
			{				
				'title': 'About us',
				'href': 'about-us',
				'in_footer': '',
			},
			{				
				'title': 'Insurance',
				'href': 'insurance',
				'in_footer': '',
				'child':[
					{
						'title': 'US',
						'href': 'us',
					},
					{
						'title': 'Mx',
						'href': 'mx',
					},
				]
			},
			{				
				'title': 'Procedures and Permits',
				'href': 'procedures-permits',
				'in_footer': '',
				'child':[
					{
						'title': 'DMV',
						'href': 'DMV',
					},
					{
						'title': 'US',
						'href': 'us',
					},
					{
						'title': 'Mexico',
						'href': 'mx',
					},
					{
						'title': 'Permits',
						'href': '../permits',
					},
				]
			},
			{				
				'title': 'Audits',
				'href': 'audits',
				'in_footer': '',
				#'child':[
					#{
						#'title': 'Servicios de consultoría en auditoría',
						#'href': 'servicios-consultoria-auditoria',
					#},
					#{
						#'title': 'Federales',
						#'href': 'federales',
					#},
					#{
						#'title': 'Estatales',
						#'href': 'estatales',
					#},
				#]
			},
			{				
				'title': 'Buy online',
				'href': 'buy-online',
				'in_footer': '',
			},
			{				
				'title': 'Contact',
				'href': 'contact',
				'in_footer': '',
			},		
		],
	]


	def get_main_menu(self, section, lang=0):
		response = ''		
		for row in self.items[lang]:
			is_active = 'active' if row['href'] == section else ''
			child = self.get_child(row['href'], row['child']) if 'child' in row else ''		
			response += "<li id=\"m_"+row['href']+"\" class=\"" + is_active + " \"><a href=\"/"+row['href']+"\" title=\""+row['title'] +"\"><span>"+row['title']+"</span></a>" + "<div class=\"invisible\">" + child + "</div></li>"

		response = "<ul class=\"menu\">" + response + "</ul>"
		return response

	def get_footer_menu(self, lang):
		response = ''
		for row in self.items[lang]:
			if 'in_footer' in row:
				child = self.get_child(row['href'], row['child']) if 'child' in row else ''
				response += "<li id=\"m_"+row['href']+"\"><a href=\"/"+row['href']+"\" title=\""+row['title'] +"\"><span>"+row['title']+"</span></a> " + child + " </li>"	
		response = "<ul class=\"menu\">" + response + "</ul>"
		return response

	def get_child(self, section, data):
		response = ''		
		for row in data:
			response += "<li><a href=\"/"+ section + '/' + row['href']+"\" title=\""+row['title'] +"\"><span>"+row['title']+"</span></a></li>"
		response = "<ul class=\"child\">" + response + "</ul>"
		return response

	def get_footer(self, section):
		response = ''		
		for row in self.items:
			if row['href'] not in 'testimoniales,contacto':
				child = self.get_child(row['href'], row['child']) if row.has_key('child') else ''
				if row['href'] == section:
					response += "<li class=\"active \"><a title=\"/"+row['title'] +"\" href=\"/"+row['href']+"\">"+row['title'].title()+"</a> "+ child +"</li>"
				else:
					response += "<li><a title=\"/"+row['title'] +"\" href=\"/"+row['href']+"\">"+row['title'].title()+"</a>"+ child +"</li>"					
		if len(response):
			response = "<ul>" + response + "</ul>"
		return response