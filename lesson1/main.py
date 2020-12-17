from selenium import webdriver
from time import sleep
import chromedriver_binary
import csv
import pandas as pd
import config
def main():
  driver = webdriver.Chrome()
  error_flg = False
  # 一休レストランのTOPページ
  driver.get(config.top_url)
  sleep(1)
  # 「検索する」のボタンをクリック
  if error_flg is False:
    try:
      notnow_button = driver.find_element_by_xpath(config.search_xpath)
      sleep(1)
      notnow_button.click()
      sleep(1)
    except Exception:
      pass
  # 「リッツカールトン京都」で検索
  if error_flg is False:
    try:
      notnow_button = driver.find_element_by_xpath(config.area_name_xpath)
      sleep(1)
      notnow_button.click()
      sleep(1)
      notnow_button.send_keys('リッツカールトン京都')
      sleep(1)
      search_button = driver.find_element_by_xpath(config.search_botton_xpath)
      sleep(1)
      search_button.click()
      sleep(1)
    except Exception:
      pass
  # 「ロカンダ」をクリック
  if error_flg is False:
    try:
      notnow_button = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div/main/section[1]/a/div[2]/h3')
      sleep(1)
      notnow_button.click()
      sleep(1)
    except Exception:
      pass
  # 「クチコミ」をクリック
  if error_flg is False:
    try:
      notnow_button = driver.find_element_by_xpath(config.review_xpath)
      sleep(1)
      notnow_button.click()
      sleep(1)
    except Exception:
      pass
  # 「もっと見る」をクリック
  if error_flg is False:
    try:
      notnow_button = driver.find_element_by_xpath(config.more_xpath)
      sleep(1)
      notnow_button.click()
      sleep(1)
    except Exception:
      pass
  # 「先頭へ」をクリック
  if error_flg is False:
    try:
      notnow_button = driver.find_element_by_xpath(congig.toppage_xpath)
      sleep(1)
      notnow_button.click()
      sleep(1)
    except Exception:
      pass
  # このページの評価（コメント、味、サービス）のスクレイピング
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
  # 一休レストランのTOPページ
  driver.get(config.top_url)
  sleep(1)
  # 「検索する」のボタンをクリック
  if error_flg is False:
    try:
      notnow_button = driver.find_element_by_xpath(config.search_xpath)
      sleep(1)
      notnow_button.click()
      sleep(1)
    except Exception:
      pass
  # 「フォーシーズンズホテル京都」で検索
  if error_flg is False:
    try:
      notnow_button = driver.find_element_by_xpath(config.area_name_xpath)
      sleep(1)
      notnow_button.click()
      sleep(1)
      notnow_button.send_keys('フォーシーズンズホテル京都')
      sleep(1)
      search_button = driver.find_element_by_xpath(config.search_botton_xpath)
      sleep(1)
      search_button.click()
      sleep(1)
    except Exception:
      pass
  # 「ブラッスリー」をクリック
  if error_flg is False:
    try:
      notnow_button = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div/main/section/a/div[2]/h3')
      sleep(1)
      notnow_button.click()
      sleep(1)
    except Exception:
      pass
  # 「クチコミ」をクリック
  if error_flg is False:
    try:
      notnow_button = driver.find_element_by_xpath(config.review_xpath)
      sleep(1)
      notnow_button.click()
      sleep(1)
    except Exception:
      pass
  # 「もっと見る」をクリック
  if error_flg is False:
    try:
      notnow_button = driver.find_element_by_xpath(config.more_xpath)
      sleep(1)
      notnow_button.click()
      sleep(1)
    except Exception:
      pass
  # 「先頭へ」をクリック
  if error_flg is False:
    try:
      notnow_button = driver.find_element_by_xpath(config.toppage_xpath)
      sleep(1)
      notnow_button.click()
      sleep(1)
    except Exception:
      pass
  # このページの評価（コメント、味、サービス）のスクレイピング
  assesment_url = 'https://restaurant.ikyu.com/107112/review/'
  driver.implicitly_wait(3)
  driver.get(assesment_url)
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
if __name__ == "__main__":
  main()