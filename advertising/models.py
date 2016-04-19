from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from .validators import valid_extension


@python_2_unicode_compatible
class Advertising(models.Model):

	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=80)
	url = models.URLField(max_length=450)
	image = models.FileField( 
		upload_to=generate_path,
		validators=[valid_extension]
	)

	class Meta(object):
		ordering = ['id']
		verbose_name = "Advertising"
		verbose_name_plural = "Advertising"

	def __str__(self):
		return self.title

