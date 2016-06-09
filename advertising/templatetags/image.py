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
        if data.timeout:
            timeout = data.timeout * 1000
            html += """
                <script>
                window.TimeOutAdvertising = """ + str(timeout) + """
                </script>"""

        html += """
            <style>
            .parent_advertising {
            position: relative;
            width: """ + width + """px;
            height: """ + height + """px;
            }
            .img_advertising {
            position: absolute;
            width: """ + width + """px;
            height: """ + height + """px;
            }
            </style>
        """

        if hasattr(data, 'images'):
            html += '<div id="images_advertising" class="parent_advertising">'
            counter = 0
            for image in data.images.all():
                html += '<div id="image_container_advertising_' + str(counter)
                html += '" <a href="' + image.url + '">'
                html += '<img src="' + settings.MEDIA_URL + str(image.photo)
                html += '" class="img_advertising"'
                html += ' id="img_advertising_' + str(counter) + '"></a>'
                html += '</div>'
                counter = counter + 1
            html += '</div>'
    else:
        html = ""

    return mark_safe(html)