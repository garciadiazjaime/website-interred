from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#0:Spanish
#1:English

urlpatterns = patterns('',
	#SPANISH
    url(r'^$', 'front.views.home', {'lang':0}, name='inicio'),
    url(r'^inicio$', 'front.views.home', {'lang':0}, name='inicio'),
    url(r'^nosotros$', 'front.views.about_us', {'lang':0}, name='nosotros'),
    	url(r'^nosotros/(?P<tag>[^/]+)$', 'front.views.about_us', {'lang':0}, name='nosotros'),
    url(r'^seguros$', 'front.views.insurance', {'lang':0}, name='seguros'),
    	url(r'^seguros/(?P<tag>[^/]+)$', 'front.views.insurance', {'lang':0}, name='seguros'),
    url(r'^tramites-permisos$', 'front.views.procedures', {'lang':0}, name='tramites-permisos'),
    	url(r'^tramites-permisos/(?P<tag>[^/]+)$', 'front.views.procedures', {'lang':0}, name='tramites-permisos'),
    url(r'^permisos$', 'front.views.permits', {'lang':0}, name='permisos'),
    	url(r'^permisos/(?P<tag>[^/]+)$', 'front.views.permits', {'lang':0}, name='permisos'),
	url(r'^auditorias$', 'front.views.audits', {'lang':0}, name='auditorias'),
    	url(r'^auditorias/(?P<tag>[^/]+)$', 'front.views.audits', {'lang':0}, name='auditorias'),
	url(r'^compra-linea$', 'front.views.buy_online', {'lang':0}, name='compra-linea'),
    	url(r'^compra-linea/(?P<tag>[^/]+)$', 'front.views.buy_online', {'lang':0}, name='compra-linea'),
    url(r'^contacto$', 'front.views.contact', {'lang':0}, name='contacto'),
    	url(r'^contacto/(?P<tag>[^/]+)$', 'front.views.contact', {'lang':0}, name='contacto'),

    #ENGLISH
    url(r'^$', 'front.views.home', {'lang':1}, name='inicio'),
    url(r'^home$', 'front.views.home', {'lang':1}, name='inicio'),
    url(r'^about-us$', 'front.views.about_us', {'lang':1}, name='nosotros'),
    	url(r'^about-us/(?P<tag>[^/]+)$', 'front.views.about_us', {'lang':1}, name='nosotros'),
    url(r'^insurance$', 'front.views.insurance', {'lang':1}, name='seguros'),
    	url(r'^insurance/(?P<tag>[^/]+)$', 'front.views.insurance', {'lang':1}, name='seguros'),
    url(r'^procedures-permits$', 'front.views.procedures', {'lang':1}, name='tramites-permisos'),
    	url(r'^procedures-permits/(?P<tag>[^/]+)$', 'front.views.procedures', {'lang':1}, name='tramites-permisos'),
    url(r'^permits$', 'front.views.permits', {'lang':1}, name='permisos'),
        url(r'^permits/(?P<tag>[^/]+)$', 'front.views.permits', {'lang':1}, name='permisos'),
	url(r'^audits$', 'front.views.audits', {'lang':1}, name='auditorias'),
    	url(r'^audits/(?P<tag>[^/]+)$', 'front.views.audits', {'lang':1}, name='auditorias'),
	url(r'^buy-online$', 'front.views.buy_online', {'lang':1}, name='compra-linea'),
    	url(r'^buy-online/(?P<tag>[^/]+)$', 'front.views.buy_online', {'lang':1}, name='compra-linea'),
    url(r'^contact$', 'front.views.contact', {'lang':1}, name='contacto'),
    	url(r'^contact/(?P<tag>[^/]+)$', 'front.views.contact', {'lang':1}, name='contacto'),

    url(r'^send_mail_form$', 'front.views.send_mail_form', name="send_mail" ),
)
