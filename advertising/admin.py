from django.contrib import admin
from .models import Advertising, ImageAdvertising


class ImageAdvertisingInline(admin.TabularInline):
    """
    Inline de fotos de artículos
    """
    model = ImageAdvertising
    extra = 3


class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ['id', 'name']
    search_fields = ['id', 'name']
    inlines = [ImageAdvertisingInline, ]


admin.site.register(Advertising, AdvertisingAdmin)