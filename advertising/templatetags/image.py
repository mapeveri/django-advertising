from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

from ..models import Advertising

register = template.Library()


@register.simple_tag
def get_images_advertising(classe = None, total = None):
	"""
	@method: get_images_advertising
	@descrip: Method thar return images advertising
	@param total: Total image to display
	@param classe: Clase css
	"""
	
	if total is None:
		data = Advertising.objects.all()
	else:
		data = Advertising.objects.all[total]	
	
	html = ""
	html += '<div class="'+classe+'">'
	for image in data:
		html += '<a href="'+image.url+'">'
		html += '<img src="'+ settings.MEDIA_URL + str(image.image) +'"  alt="img"></a>'
	html += '</div>'
            
	return mark_safe(html)

