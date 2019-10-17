from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pandas as pd
import os


url = "https://www.thegazette.co.uk/insolvency/notice?results-page-size=100&numberOfLocationSearches=1&start-publish-date=2014-01-01&location-distance-1=1&sort-by=oldest-date&categorycode=G405010206+G405010311+G405010405+-2&service=insolvency&end-publish-date=2019-09-30&results-page=1"

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)


print(response.status_code)