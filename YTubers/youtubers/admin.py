from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html
# Register your models here.


class YTAdmin(admin.ModelAdmin):

    def YTphoto(self,object):
        return format_html('<img width="40" src="{}" />'.format(object.photo.url))


    list_display = ('id','name','subs_count','YTphoto','is_featured')
    list_display_links = ('name','id')
    search_fields = ('name','camera_type')
    list_filter = ('city','camera_type')
    list_editable = ('is_featured',)

admin.site.register(Youtuber,YTAdmin)
