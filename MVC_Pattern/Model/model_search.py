from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

def search(s):
	srch = s
	driver = webdriver.Chrome(executable_path="/home/rafs/Desktop/Project/chromedriver.exe")

	driver.get("https://www.google.com")

	inputElems = driver.find_elements_by_css_selector("input[name=q]")
		
	for inputElem in inputElems:
		inputElem.send_keys(s)
		inputElem.send_keys(Keys.ENTER)

	time.sleep(5)


class Model_search(object):
	def __init__(self, s):
		search(s)
		