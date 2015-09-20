Starting the Project!
=====================

Every thing is installed and the first functional test is written
and failing as expected so now we have to fix our test!

So let's make a django project called superlist by running the following command:

django-admin.py startproject superlist

And you should end up with a file tree that looks like this

.
├── functional_tests.py
├── README.rst
├── requirements.txt
└── superlist
    ├── manage.py
    └── superlist
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py

From now on we are going to be doing the vast majority of our work in the top level superlist directory
so lets move functional_tests.py into that directory as well as requirements.txt