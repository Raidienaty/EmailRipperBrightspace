from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time, sys, os

url = input("URL: ")

dirname = os.path.dirname(__file__)
driverPath = os.path.join(dirname, 'geckodriver.exe')

binary = FirefoxBinary('/mnt/c/Program\ Files/Mozilla\ Firefox/firefox.exe')

driver = webdriver.Firefox(executable_path=driverPath, firefox_binary=binary)

driver.get(url)

table = find_element_by_id("z_h")

print(table.summary)

driver.close()
