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

Now we are ready to run Django and see if our functional_tests will pass. You are going to need two terminal windows for this.



on the command line run the following command

python manage.py runserver

And then go to a second terminal and run the command

python functional_tests.py


It should pass!

python manage runserver