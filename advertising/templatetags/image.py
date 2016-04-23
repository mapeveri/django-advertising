import sys

from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

from ..models import Advertising

register = template.Library()


@register.simple_tag
def get_images_advertising(classe = None, total = None, *args, **kwargs):
	"""
	@method: get_images_advertising
	@descrip: Method thar return images advertising
	@param total: Total image to display
	@param classe: Clase css
	"""
	   
	width = kwargs['width']
	height = kwargs['height']
	
	if sys.version_info >= (3,0):
	    if not isinstance(width, str):
	       width = str(width)
	else:
	    if not isinstance(width, basestring):
	       width = str(width)
	
	if sys.version_info >= (3,0):
	    if not isinstance(height, str):
	       height = str(height)
	else:
	    if not isinstance(height, basestring):
	       height = str(height)
	
	if total is None:
		data = Advertising.objects.all()
	else:
		data = Advertising.objects.all[total]	
	
	html = ""
	
	html += """
	    <style>
	    .img_advertising {
              position: absolute;
              width: """ + width + """px;
              height: """ + height + """px;
          }
        </style>
	"""
	
	html += '<div id="images_advertising" class="'+classe+'" style="position: relative;">'
	counter = 0
	for image in data:
	    html += '<div id="image_container_advertising_' + str(counter) + '"'
	    html += '<a href="' + image.url + '">'
	    html += '<img src="'+ settings.MEDIA_URL + str(image.image) +'" class="img_advertising"'
	    html += ' id="img_advertising_' + str(counter) + '"></a>'
	    html += '</div>'
	    counter = counter + 1
	html += '</div>'
            
	return mark_safe(html)

