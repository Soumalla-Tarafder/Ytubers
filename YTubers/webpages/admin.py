from django.contrib import admin
from .models import Slider,Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):

    def myphoto(self,object):
        return format_html('<img width="40" src="{}" />'.format(object.photo.url))

    list_display = ('id','myphoto','firstname','lastname','created_date')
    list_display_links = ('firstname','id')
    search_fields = ('firstname','fb_link')
    list_filter = ('firstname',)

admin.site.register(Slider)
admin.site.register(Team,TeamAdmin)