# Django Sandbox

Use PyCharm for it, but do not have to.


To install Django, run in terminal:

    $ python -m pip install django

o start a new project `myprojectname`:

    $ django-admin startproject djsandbox

It will create the needed files and subfolder `djsandbox`. Go there and run:

    $ cd djsandbox
    $ python manage.py runserver

It runs a development server. It shows the url where it hosts it, http://127.0.0.1:8000. `Ctrl-C` to stop it.

To create a Django app, run this in the Django(`djsanbox`) folder, it creates a Python package,
you can then import it and use:

    $ python manage.py startapp website

Add it in the APP list, and to the url patterns, etc.
