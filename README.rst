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
	
	python manage.py migrate

3. Add this script in your file .html to use::

	<script src="{% static 'advertising/js/events.js' %}"></script>

4. Add this line in your file .html to use::
	
	{% load image %}
	{% get_images_advertising width=300 height=300 campaign=3 %}


Parameters
----------

1. width and height: Element size.
2. Campaign: Id Advertising Model.

Contribute
----------

1. Fork this repo and install it
2. Follow PEP8, Style Guide for Python Code
3. Write code
4. Write unit test
5. Send pull request
 