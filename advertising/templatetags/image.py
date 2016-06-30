import sys

from django import template
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils.safestring import mark_safe

from ..models import Advertising

register = template.Library()


@register.simple_tag
def get_images_advertising(width=100, height=100, *args, **kwargs):
    """
    @method: get_images_advertising
    @descrip: Method thar return images advertising
    @param width: width img
    @param height: height img
    """

    if 'campaign' in kwargs:
        campaign = kwargs['campaign']
    else:
        campaign = None

    if sys.version_info >= (3, 0):
        if not isinstance(width, str):
            width = str(width)
    else:
        if not isinstance(width, basestring):
            width = str(width)

    if sys.version_info >= (3, 0):
        if not isinstance(height, str):
            height = str(height)
    else:
        if not isinstance(height, basestring):
            height = str(height)

    if campaign is None:
        try:
            data = Advertising.objects.all()[0]
        except Advertising.DoesNotExist:
            data = None
    else:
        try:
            data = Advertising.objects.get(id_advertising=campaign)
        except Advertising.DoesNotExist:
            data = None

    html = ""

    if data:
        id_adv = data.id_advertising.strip()
        if data.timeout:
            timeout = data.timeout * 1000
            html += """
                <script>
                window.TimeOutAdvertising_""" + id_adv + """ = """ + str(timeout) + """
                </script>"""

        # Style css
        class_parent = "position: relative; width: " + width + "px; height: " + height + "px;"
        class_img = "position: absolute; width: " + width + "px; height: " + height + "px;"
        
        if hasattr(data, 'images'):
            html += '<div id="images_advertising_' + id_adv + '"'
            html += ' style="' + class_parent + '">'
            counter = 0
            for image in data.images.all():
                html += '<div id="image_container_advertising_' + str(counter)
                html += '_' + id_adv + '"'
                html += '> <a target="_blank" href="' + image.url + '">'
                html += '<img src="' + settings.MEDIA_URL + str(image.photo)
                html += '" style="' + class_img + '"'
                html += ' id="img_advertising_' + str(counter) + '_' + id_adv
                html += '"></a>'
                html += '</div>'
                counter = counter + 1
            html += '</div>'

            html += """
            <script>
            document.addEventListener("DOMContentLoaded", function(event) { 
                advertisingModule.initialize('""" + id_adv + """');
            });
            </script>
            """
    else:
        html = ""

    return mark_safe(html)
