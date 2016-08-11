# -*- coding: utf-8 -*-

class DataDB(object):

	def general(self, lang):
		data = [
				{#SPANISH
					'footer':
						{
							'title': 'Contáctanos',
							'address': '<p>9765  Marconi  Dr. 105<br />San Diego, CA 92154, USA</p><p>+(619) 710 0451 <br />Fax +(619) 710 4827</p>',
						},
				},
				{#ENGLISH
					'footer':
						{
							'title': 'Contact us',
							'address': '<p>9765  Marconi  Dr. 105<br />San Diego, CA 92154, USA</p><p>+(619) 710 0451 <br />Fax +(619) 710 4827</p>',
						},
				},
			]
		return data[lang]

	def home(self, lang):
		data = [
				{#SPANISH
					'gral_info':
						{
							'page_title': 'Inter-Red Insurance',
							'keywords': 'Inter-Red Insurance',
							'description': 'Bienvenido al sitio oficial de Inter-Red Insurance',
							'section': 'inicio',
							'section_lang': 'home',
							'sp_active': 'active',
							'wrapper_class': 'wrapper_inicio',
						},
					'header':
						{
							'title': 'Su mejor alternativa en <span>Seguros Comerciales</span>',
							'about_us_title': 'Nosotros',
							'about_us_text': '<p>Inter RED Insurance es una empresa consolidada y líder en la industria;</p><p>La empresa de servicios ofrece soluciones al sector transportista tanto público como privado en lo que respecta a seguros, consultoría y permisos de transporte de carga. Con más de 20 años de trabajo, Inter RED Insurance ha logrado satisfacer las necesidades de sus clientes y superar sus expectativas.</p>',
							'about_us_btn_title': 'Conócenos',
							'about_us_btn_href': 'nosotros',
						},
				},
				{#ENGLISH
					'gral_info':
						{
							'page_title': 'Inter-Red Insurance',
							'keywords': 'Inter-Red Insurance',
							'description': 'Welcome to oficial site of Inter-Red Insurance',
							'section': 'home',
							'section_lang': 'inicio',
							'en_active': 'active',
							'wrapper_class': 'wrapper_inicio',
						},
					'header':
						{
							'title': 'Your best alternative in <span>Comercial Insurance</span>',
							'about_us_title': 'About us',
							'about_us_text': '<p>Inter RED Insurance is an established company leader in its industry, founded in 1990.;</p><p>This company offers solutions to the transport sector, both public as well as private. With more than 20 years of service, Inter RED Insurance has met its client’s needs and exceeded their expectations.</p>',
							'about_us_btn_title': 'About us',
							'about_us_btn_href': 'about-us',
						},
				},
			]
		return data[lang]

	def about_us(self, lang):
		data = [
				{#SPANISH
					'gral_info':
						{
							'page_title': 'Inter-Red Insurance',
							'keywords': 'Inter-Red Insurance',
							'description': 'Bienvenido al sitio oficial de Inter-Red Insurance',
							'menu_home': 'active',
							'section': 'nosotros',
							'section_lang': 'about-us',
							'sp_active': 'active',
							'wrapper_class': 'wrapper_about_us',
						},
				},
				{#ENGLISH
					'gral_info':
						{
							'page_title': 'Inter-Red Insurance',
							'keywords': 'Inter-Red Insurance',
							'description': 'Welcome to oficial site of Inter-Red Insurance',
							'menu_home': 'active',
							'section': 'about-us',
							'section_lang': 'nosotros',
							'en_active': 'active',
							'wrapper_class': 'wrapper_about_us',
						},
				},
			]
		return data[lang]

	def insurance(self, lang):
		data = [
				{#SPANISH
					'gral_info':
						{
							'page_title': 'Inter-Red Insurance',
							'keywords': 'Inter-Red Insurance',
							'description': 'Bienvenido al sitio oficial de Inter-Red Insurance',
							'menu_home': 'active',
							'section': 'seguros',
							'section_lang': 'insurance',
							'sp_active': 'active',
						},
				},
				{#ENGLISH
					'gral_info':
						{
							'page_title': 'Inter-Red Insurance',
							'keywords': 'Inter-Red Insurance',
							'description': 'Welcome to oficial site of Inter-Red Insurance',
							'menu_home': 'active',
							'section': 'insurance',
							'section_lang': 'seguros',
							'en_active': 'active',
						},
				},
			]
		return data[lang]

	def procedures(self, lang):
		data = [
				{#SPANISH
					'gral_info':
						{
							'page_title': 'Inter-Red Insurance',
							'keywords': 'Inter-Red Insurance',
							'description': 'Bienvenido al sitio oficial de Inter-Red Insurance',
							'menu_home': 'active',
							'section': 'tramites-permisos',
							'section_lang': 'procedures-permits',
							'sp_active': 'active',
							'wrapper_class': 'tramites-permisos',
						},
				},
				{#ENGLISH
					'gral_info':
						{
							'page_title': 'Inter-Red Insurance',
							'keywords': 'Inter-Red Insurance',
							'description': 'Welcome to oficial site of Inter-Red Insurance',
							'menu_home': 'active',
							'section': 'procedures-permits',
							'section_lang': 'tramites-permisos',
							'en_active': 'active',
							'wrapper_class': 'tramites-permisos',
						},
				},
			]
		return data[lang]

	def permits(self, lang):
		data = [
				{#SPANISH
					'gral_info':
						{
							'page_title': 'Inter-Red Insurance Permisos',
							'keywords': 'Inter-Red Insurance Permisos',
							'description': 'Bienvenido al sitio oficial de Inter-Red Insurance Permisos',
							'menu_home': 'active',
							'section': 'permisos',
							'section_lang': 'permits',
							'sp_active': 'active',
							'wrapper_class': 'tramites-permisos',
						},
				},
				{#ENGLISH
					'gral_info':
						{
							'page_title': 'Inter-Red Permits',
							'keywords': 'Inter-Red Permits',
							'description': 'Welcome to oficial site of Inter-Red Insurance',
							'menu_home': 'active',
							'section': 'permits',
							'section_lang': 'permisos',
							'en_active': 'active',
							'wrapper_class': 'tramites-permisos',
						},
				},
			]
		return data[lang]

	def audits(self, lang):
		data = [
				{#SPANISH
					'gral_info':
						{
							'page_title': 'Inter-Red Insurance',
							'keywords': 'Inter-Red Insurance',
							'description': 'Bienvenido al sitio oficial de Inter-Red Insurance',
							'menu_home': 'active',
							'section': 'auditorias',
							'section_lang': 'audits',
							'sp_active': 'active',
						},
				},
				{#ENGLISH
					'gral_info':
						{
							'page_title': 'Inter-Red Insurance',
							'keywords': 'Inter-Red Insurance',
							'description': 'Welcome to oficial site of Inter-Red Insurance',
							'menu_home': 'active',
							'section': 'audits',
							'section_lang': 'auditorias',
							'en_active': 'active',
						},
				},
			]
		return data[lang]

	def buy_online(self, lang):
		data = [
				{#SPANISH
					'gral_info':
						{
							'page_title': 'Inter-Red Insurance',
							'keywords': 'Inter-Red Insurance',
							'description': 'Bienvenido al sitio oficial de Inter-Red Insurance',
							'menu_home': 'active',
							'section': 'compra-linea',
							'section_lang': 'buy-online',
							'sp_active': 'active',
						},
				},
				{#ENGLISH
					'gral_info':
						{
							'page_title': 'Inter-Red Insurance',
							'keywords': 'Inter-Red Insurance',
							'description': 'Welcome to oficial site of Inter-Red Insurance',
							'menu_home': 'active',
							'section': 'buy-online',
							'section_lang': 'compra-linea',
							'en_active': 'active',
						},
				},
			]
		return data[lang]

	def contact(self, lang):
		data = [
				{#SPANISH
					'gral_info':
						{
							'page_title': 'Inter-Red Insurance',
							'keywords': 'Inter-Red Insurance',
							'description': 'Bienvenido al sitio oficial de Inter-Red Insurance',
							'menu_home': 'active',
							'section': 'contacto',
							'section_lang': 'contact',
							'sp_active': 'active',
						},
				},
				{#ENGLISH
					'gral_info':
						{
							'page_title': 'Inter-Red Insurance',
							'keywords': 'Inter-Red Insurance',
							'description': 'Welcome to oficial site of Inter-Red Insurance',
							'menu_home': 'active',
							'section': 'contact',
							'section_lang': 'contacto',
							'en_active': 'active',
						},
				},
			]
		return data[lang]
'''

################################ GENERAL - Español ###################
	def general(self):
		menu = {
			'inicio':{
				'name': 'Inicio',
				'href': 'inicio',
			},
			'nosotros':{
				'name': 'Nosotros',
				'href': 'nosotros',
				'child': '<li><a href="/nosotros/mision" title="Misión">Misión</a></li><li><a href="/nosotros/siete-principios" title="Siete principios de Cruz Roja">Siete principios de Cruz Roja</a></li><li><a href="/nosotros/institucionalidad-transparencia" title="Institucionalidad y Transparencia">Institucionalidad y Transparencia</a></li><li><a href="/nosotros/equipo-trabajo" title="Equipo de trabajo">Equipo de trabajo</a></li><li><a href="/nosotros/voluntariado" title="Voluntariado">Voluntariado</a></li><li><a href="/nosotros/historia" title="Historia">Historia</a></li>',
			},
			'hospital':{
				'name': 'Hospital',
				'href': 'hospital',
				'child': '<li><a href="/hospital/servicios" title="Servicios">Servicios</a></li><li><a href="/hospital/medicos-especialistas" title="Médicos especialistas">Médicos especialistas</a></li><li><a href="/hospital/instalaciones" title="Instalaciones">Instalaciones</a></li><li><a href="/hospital/banco-sangre" title="Banco de Sangre">Banco de Sangre</a></li>',
			},
			'ambulancias':{
				'name': 'Ambulancias',
				'href': 'ambulancias',
				'child': '<li><a href="/ambulancias/equipo" title="Equipo">Equipo</a></li><li><a href="/ambulancias/bases-ambulancia" title="Bases de Ambulancia">Bases de Ambulancia</a></li>',
			},
			'donativos':{
				'name': 'Donativos',
				'href': 'donativos',
			},
			'transparencia':{
				'name': 'Transparencia',
				'href': 'transparencia',
				'child': '<li><a href="/transparencia/servicios-comunidad" title="Servicios a la Comunidad">Servicios a la Comunidad</a></li><li><a href="/transparencia/ingresos-egresos" title="Ingresos y Egresos">Ingresos y Egresos</a></li><li><a href="/transparencia/donativos" title="Donativos">Donativos</a></li><li><a href="/transparencia/recuperacion" title="Recuperación">Recuperación</a></li><li><a href="/transparencia/proyectos" title="Proyectos">Proyectos</a></li>',
			},
			'contacto':{
				'name': 'Contacto',
				'href': 'contacto',
				'child': '<li><a href="/contacto/ubicacion" title="Ubicación">Ubicación</a></li><li><a href="/contacto/forma-contacto" title="Forma de Contacto">Forma de Contacto</a></li><li><a href="/contacto/directorio" title="Directorio">Directorio</a></li>',
			},
			'noticias':{
				'name': 'Noticias',
				'href': 'noticias',
			},
		}
		return data



################################ GENERAL - Inglés ###################
	def general_ing(self):
		menu = {
			'inicio':{
				'name': 'Home',
				'href': 'home',
			},
			'nosotros':{
				'name': 'Us',
				'href': 'us',
				'child': '<li><a href="/us/mission" title="Mission">Mission</a></li><li><a href="/us/fundamental-principles" title="Fundamental Principles">Fundamental Principles</a></li><li><a href="/us/transparency-institutionalism" title="Transparency and Institutionalism">Transparency and Institutionalism</a></li><li><a href="/us/work-force" title="Work Force ">Work Force </a></li><li><a href="/us/voluntary-work" title="Voluntary Work">Voluntary Work</a></li><li><a href="/us/history" title="History">History</a></li>',
			},
			'hospital':{
				'name': 'Hospital',
				'href': 'hospital',
				'child': '<li><a href="/hospital/services" title="Services">Services</a></li><li><a href="/hospital/especialized-consultation" title="Especialized Consultation">Especialized Consultation</a></li><li><a href="/hospital/facilities" title="Hospitalization Area Facilities">Hospitalization Area Facilities</a></li><li><a href="/hospital/blood-bank" title="Blood Bank">Blood Bank</a></li>',
			},
			'ambulancias':{
				'name': 'Ambulance Services',
				'href': 'ambulance-services',
				'child': '<li><a href="/ambulance-services/equipment" title="Equipment">Equipment</a></li><li><a href="/ambulance-services/strategic-ambulance-stations" title="Strategic Ambulance Stations">Strategic Ambulance Stations</a></li>',
			},
			'donativos':{
				'name': 'Donation',
				'href': 'donation',
			},
			'transparencia':{
				'name': 'Transparency',
				'href': 'transparency',
				'child': '<li><a href="/transparency/community-service" title="Community Service">Community Service</a></li><li><a href="/transparency/income-outcome" title="Income and Outcome">Income and Outcome</a></li><li><a href="/transparency/donation" title="Donation">Donation</a></li><li><a href="/transparency/recovery-rates" title="Recovery Rates">Recovery Rates</a></li><li><a href="/transparency/projects" title="Projects">Projects</a></li>',
			},
			'contacto':{
				'name': 'Contact Us',
				'href': 'contact-us',
				'child': '<li><a href="/contact-us/ubicacion" title="Ubicación">Ubicación</a></li><li><a href="/contact-us/forma-contacto" title="Forma de Contacto">Forma de Contacto</a></li><li><a href="/contact-us/directorio" title="Directorio">Directorio</a></li>',
			},
			'noticias':{
				'name': 'Noticias',
				'href': 'noticias',
			},
		}
		return data

################################ INICIO - Español ###################

	def inicio(self):
		data = {
			'info_gral': {
				'page_title': 'Garita Otay',
				'keywors': 'Garita Otay',
				'description': 'Welcome to Garita Otay',
				'menu_inicio': 'current',
				'section': 'inicio',
				'section_lang': 'home',
			},

		}
		return data


################################ INICIO - Inglés #####################

	def home(self):
		data = {
			'info_gral': {
				'page_title': 'Garita Otay',
				'keywors': 'Garita Otay',
				'description': 'Welcome to Garita Otay',
				'menu_inicio': 'current',
				'section': 'inicio',
				'section_lang': 'home',
			},
		}
		return data
'''
