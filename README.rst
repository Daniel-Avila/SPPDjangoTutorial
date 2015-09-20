Testing Frameworks
==================

OK our first test does test something but it is not very helpful.

We could manually add support code to print out messages when a tests passes
and a more useful message when a test fails.

But Testing is well supported in python and there are testing frameworks that will handle that for us.

The defacto test framework in python is called *unittest*. Despite the name it can be used for any number of types
of tests. In this case we are going to use it to help improve our functional tests.

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

