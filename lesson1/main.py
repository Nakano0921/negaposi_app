from selenium import webdriver
from time import sleep
import chromedriver_binary
import csv
import pandas as pd
import config
def main():
  driver = webdriver.Chrome()
  return driver
def open_target(driver):
  """
  toppageを開いて
  「銀座」を開いて
  レストランを開いて
  クチコミを表示
  """
  # 一休レストランのTOPページ
  driver.get(config.top_url)
  sleep(1)
  # 「銀座」を押す
  button = driver.find_element_by_xpath(config.ginza_xpath)
  sleep(1)
  button.click()
  sleep(1)
  # （一番）のレストランを取得
  button = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/main/section[1]/a/div[1]/span/img')
  sleep(1)
  butto.click()
  sleep(1)
  # クチコミを表示
  a = driver.find_element_by_id('layout').text
  if a != '規定評価数に達していません':
    button = driver.find_element_by_xpath(config.review_xpath)
    sleep(1)
    button.click()
    sleep(1)
    button = driver.find_element_by_xpath(config.more_xpath)
    sleep(1)
    button.click()
    sleep(1)
    button = driver.find_element_by_xpath(congig.toppage_xpath)
    sleep(1)
    button.click()
    sleep(1)
def get_item():
  """
  コメント、味、サービスのスクレイピング
  """
  assesment_url = driver.current_url
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
  def writeCSV():
    """
    csvに保存
    """
    df = pd.DataFrame()
    df[comment] = comments
    df[taste] = tastes
    df[service] = services
    df.to_csv('assesment.csv', index=False)

if __name__ == "__main__":
  main()
  open_target(driver)
  get_item()
  comments = []
  tastes = []
  services = []
  writeCSV()
