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

Testing Frameworks
==================

OK our first test does test something but it is not very helpful.

We could manually add support code to print out messages when a tests passes
and a more useful message when a test fails.

But Testing is well supported in python and there are testing frameworks that will handle that for us.

The defacto test framework in python is called *unittest*. Despite the name it can be used for any type
of test. In this case we are going to use it to help improve our functional tests.

IMHO *unittest* should be renamed something like *autotest* but nobody listens to me.


At the top of the file functional_test.py add the line

import unittest

And we are going to define a class called *HomePage* which extends *unttest.TestCase*

Doing this gives us access to the test harness and quite a few enhancements to make testing easier.

In our case we need to open up a browser before each test and close it down after each test. Our parent class *TestCase*
provides us with some hooks to do this

*setUp*
*tearDown*

|History: setUp and tearDown break the python convention by using camel case. This is because unittest was originally a
port of JUnit for Python.

And we need to add a method to our test class named *test_home_page*

Now stop and consider that we have access to a couple of hooks *setUp* and *tearDown*. The sorts of code that should go there
are lines that will be used for each test. Since we will be adding more than one selenium test we will probably want to
open a browser at the start of each test. So lets put that in our setUp method.

def setUp(self):
    self.browser = webdriver.Firefox()

A general principle in testing is that each test is self contained and cleans up after itself. So let's quit the browser
after each test by putting that into our tearDown method

def tearDown(self):
    self.browser.quit() # NOTE: NOT close() the close method just minimizes the browser

And now lets move the rest of the code into our test method


Finally to have our unittest class run we have to add a call to *unittest.main*

if __name__ == '__main__':
    unittest.main()