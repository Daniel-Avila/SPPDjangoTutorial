__author__ = 'sparky'
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')
result = browser.title
browser.close()
assert 'Django' in result
