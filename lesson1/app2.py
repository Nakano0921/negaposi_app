from selenium import webdriver
from time import sleep
import chromedriver_binary
import csv
import pandas as pd
driver = webdriver.Chrome()
error_flg = False
url = 'https://restaurant.ikyu.com/103396/'
driver.get(url)
sleep(1)
if error_flg is False:
  try:
    notnow_button = driver.find_element_by_xpath('//*[@id="main-article"]/nav/ul/li[3]')
    sleep(1)
    notnow_button.click()
    sleep(1)
  except Exception:
    pass
if error_flg is False:
  try:
    notnow_button = driver.find_element_by_xpath('//*[@id="guideContent"]/section/div[2]/div[1]/div[1]/div[2]/div/div[3]/a')
    sleep(1)
    notnow_button.click()
    sleep(1)
  except Exception:
    pass
if error_flg is False:
  try:
    notnow_button = driver.find_element_by_xpath('//*[@id="des_inner"]/div[24]/a[2]')
    sleep(1)
    notnow_button.click()
    sleep(1)
  except Exception:
    pass
assesment_url = 'https://restaurant.ikyu.com/103396/review/'
driver.implicitly_wait(3)
driver.get(assesment_url)
comments = []
tastes = []
services = []
assesments = driver.find_elements_by_class_name('des_gdIDUsrImprBox')
i = 4
for assesment in assesments:
  if i == 24:
    break
  comment = assesment.find_element_by_xpath(f'//*[@id="des_inner"]/div[{i}]/div[3]/table/tbody/tr[3]/td').text
  comments.append(comment)
  taste = assesment.find_element_by_xpath(f'//*[@id="des_inner"]/div[{i}]/div[1]/table/tbody/tr[2]/td[2]/span').text
  tastes.append(taste)
  service = assesment.find_element_by_xpath(f'//*[@id="des_inner"]/div[{i}]/div[1]/table/tbody/tr[3]/td[2]/span').text
  services.append(service)
  i +=2
print(comments,tastes,services)
df = pd.DataFrame()
df[comment] = comments
df[taste] = tastes
df[service] = services
df.to_csv('assesment.csv', index=False)
