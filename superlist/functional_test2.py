__author__ = 'sparky'
import unittest
from selenium import webdriver

class HomePage(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        """Does To-Do show up in the browser's title for the home page?"""
        expected = 'To-Do'
        self.browser.get('http://localhost:8000')
        result = self.browser.title
        self.assertIn(expected, result)

if __name__ == '__main__':
    unittest.main()

#    def test_<reasonable_name>(self):
        # """Human readable description of the test goes here.

        # The first line should be the description. It can be multi line.
        # I like to make the first line a question
        # """
         #Define expected values

         #Run the code under test to get the actual value

         #Compair the expected value with the actual value