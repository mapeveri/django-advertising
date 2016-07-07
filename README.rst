Django-Advertising
==================

Django application for show advertising configurable.

Installing
----------

With pip::
	
	pip install django-advertising


Quick start
-----------

1. Add 'advertising' to INSTALLED_APPS::
	
	
	INSTALLED_APPS = (
        ...
        'advertising',
     )

2. Apply migrations::
	
	python manage.py makemigrations advertising
	python manage.py migrate advertising

3. Add this script in your file .html to use::

	<script src="{% static 'advertising/js/events.js' %}"></script>

4. Add this line in your file .html to use::
	
	{% load image %}
	{% get_images_advertising height=300 campaign='CMP1' %}


Parameters
----------

1. Height: Min height element size.
2. Campaign: Id unique Advertising Model. (String)

Responsive
----------

If you wish to play with media queries, use the **img-advertising** class.

Contribute
----------

1. Fork this repo and install it
2. Follow PEP8, Style Guide for Python Code
3. Write code
4. Write unit test
5. Send pull request
 
