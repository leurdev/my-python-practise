from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()

title = []
driver.get("https://github.com/leurdev")
