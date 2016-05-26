import os

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from .validators import valid_extension


@python_2_unicode_compatible
class Advertising(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)

    class Meta(object):
        ordering = ['id']
        verbose_name = "Advertising"
        verbose_name_plural = "Advertising"

        def __str__(self):
            return self.title


@python_2_unicode_compatible
class ImageAdvertising(models.Model):

    def generate_path(instance, filename):
        folder = "campaign_" + str(instance.advertising.id)
        return os.path.join("campaigns", folder, filename)

    advertising = models.ForeignKey(Advertising, related_name='images')
    title = models.CharField(max_length=80)
    url = models.URLField(max_length=450)
    photo = models.FileField("Foto", blank=False, null=False,
                            upload_to=generate_path,
                            validators=[valid_extension])

    def __str__(self):
        return self.advertising.name
