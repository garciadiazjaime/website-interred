# -*- coding: utf-8 -*-

from django.contrib import admin
from data.models import Section, Data_DB

class SectionAdmin(admin.ModelAdmin):
	list_display = ('title_en', 'title_sp', 'slug_en', 'slug_sp', 'in_main_menu', 'in_footer')
	search_fields = ['title_en', 'title_sp', 'slug_en', 'slug_sp']
	list_filter = ['in_main_menu', 'in_footer']

class DataAdmin(admin.ModelAdmin):
	list_display = ( 'id', 'section', 'text_sp', 'text_en')
	search_fields = ['text_en', 'text_sp']
	list_filter = ['section']

admin.site.register(Section)
admin.site.register(Data_DB, DataAdmin)
