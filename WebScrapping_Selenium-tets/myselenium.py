from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()

title = []  # List to store name of the product
# prices=[] #List to store price of the product
# ratings=[] #List to store rating of the product
driver.get("https://github.com/leurdev")

content = driver.page_source
soup = BeautifulSoup(content)

print(soup.get_text())
