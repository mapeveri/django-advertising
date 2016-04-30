from django.contrib import admin
from .models import Advertising


class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ['id', 'title']
    search_fields = ['id', 'title']


admin.site.register(Advertising, AdvertisingAdmin)