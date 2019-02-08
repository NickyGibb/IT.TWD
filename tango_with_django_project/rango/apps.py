# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class RangoConfig(AppConfig):
    name = 'rango'

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category','url')

admin.site.register(Page,PageAdmin)
    
