Welcome to the SPP Django Tutorial Workshop!
============================================

Before you can start you need to make sure you have the
following installed and working on your machine.

It is assumed that you are using a MSWindows machine so the documentation
I will point to will cover MSWindows installs.

Base Tools you will need to install are:

Python 3.5
----------
https://www.python.org/downloads/release/python-350/

PIP
---
Today is your lucky day! Pip is included in Python 3.4+ Move along people
nothing to see here. :)

Virtualenv (for your platform)
------------------------------

Virtualenv allows us to create isolated python environments. Without it we are
installing everything globally and that can turn into a really big confusing mess.

I'm not going to make you look it up the command.

Open up a windows command line and run the following command

`Gotcha`
If you have more than one version of Python installed how do you know if you are using pip installed with
Python 3.5?

If you have the python launcher installed you could do this:


py -2   -m pip install SomePackage  # default Python 2
py -2.7 -m pip install SomePackage  # specifically Python 2.7
py -3   -m pip install SomePackage  # default Python 3
py -3.4 -m pip install SomePackage  # specifically Python 3.4
py -3.5 -m pip install SomePackage  # specifically Python 3.5

But not to worry if you don't. The pip you want to use should be located in
C:\\Python35\\Scripts\\pip.exe

So if bad comes to worse just do:

C:\\Python35\\Scripts\\pip install virtualenv

Virtualenv-wrapper (for your platform)
--------------------------------------
Virtual Environment Wrapper is a set of tools to make using python virtual environments
easier to use. It would be a good thing to read up on how to use it.

For now here is the command to install it!

C:\\Python35\\Scripts\\pip install virtualenvwrapper-win

Once you install it there are some helpful environment variables you will want to set.
I trust that you can read documentation so have a look here and trick-out your mighty mighty hax0r box. :)

https://pypi.python.org/pypi/virtualenvwrapper-win

Once you get that done and working you are ready to start the tutorial!
