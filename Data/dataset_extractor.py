URL = "https://www.kaggle.com/datasets?page=1"
sample = open("Data/dataset.txt","w")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import chromedriver_autoinstaller
from bs4 import BeautifulSoup

chromedriver_autoinstaller.install()


options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)


driver.get(url=URL)
sleep(5)
response = driver.page_source

soup = BeautifulSoup(response,'html.parser')
body = soup.find("div", class_='sc-gauFBm jPwQup')

datasets =[]
paths = []

for a in body.find_all('a',class_='sc-gFGZVQ NUNdY',href=True):
    paths.append(a['href'])

sample.write(str(paths))
sample.close()