A New Django App
================

Standard practice for code organization is to create separate modules for common groups of functionality.

In Django those separate modules are called *apps*.

In a perfect world those apps should be self contained without the need for other apps. In the real world they sometimes
do have dependencies.

Here we are building a To-Do list so we will need a *list* app. In the future we might decide that it would be good to
have a calendar along with our To-Do list. Then we would create a calendar app etc. and so on.

For now let's just create a list app. To create a new app in Django you simply run the manage command startapp like so:


python manage.py startapp lists

Once that is done we now have a directory structure for our project that looks like this:

.
├── README.rst
└── superlist
    ├── db.sqlite3
    ├── functional_tests.py
    ├── lists
    │   ├── admin.py
    │   ├── __init__.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── manage.py
    ├── requirements.txt
    └── superlist
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-34.pyc
        │   ├── settings.cpython-34.pyc
        │   ├── urls.cpython-34.pyc
        │   └── wsgi.cpython-34.pyc
        ├── settings.py
        ├── urls.py
        └── wsgi.py
