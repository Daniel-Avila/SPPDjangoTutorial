Step 1
============================================

Now that you have the tools installed and have chosen your favorite editor we get to set up our environment.

This is where Python virtualenv comes into play.

First we need to make our virtual environment

From the command line run the command

C:\\mkvirtualenv SPPDjango

Voila! You now have a self contained python environment to work in. You should see that your command line is now
decorated with your active python environment.

Let's close this environment for now. Run the command

C:\\deactivate

And now you have closed the virtual environment. You can make multiple virtual environments each with it's own configuration
without any danger of cross contamination. Now run the command:

C:\\workon

And you should see a list of virtual environments which you have created to activate one just run:

C:\\workon SPPDjango

Step 2
======

First it will help if you make a project directory. You can name it anything you wish. PythonProjects or Projects
would probably do well. For this text I will assume PythonProjects

C:\\mkdir PythonProjects
C:\\cd PythonProjects
C:\\mkdir superlist
C:\\cd superlist
C:\\workon SPPDjango

Step 3
======

Now you are ready to make your directory into a git repository

Make sure you are in your *superlist* directory and type the command

git init


Step 4
======

And now for stuff to install. Make sure you are in your virtual environment for the tutorial by running workon SPPDjango
if you are not sure.

use pip to install the following packages

pip install ipython
pip install selenium
pip install model_mommy
pip install django
