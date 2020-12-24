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
    # レストランを取得
    a = driver.find_element_by_class_name("ratingCount_6le43").text
    if a != "規定評価数に達していません":
        button = driver.find_element_by_xpath(
            '//*[@id="__layout"]/div/div[2]/div[1]/main/section[1]/a/div[1]/span/img'
        )
        sleep(1)
        button.click()
        sleep(5)
        tab_array = driver.window_handles
        driver.switch_to.window(tab_array[1])
        sleep(1)
        # クチコミを表示
        button = driver.find_element_by_xpath(config.review_xpath)
        sleep(1)
        button.click()
        sleep(1)
        button = driver.find_element_by_xpath(config.more_xpath)
        sleep(1)
        button.click()
        sleep(1)
        button = driver.find_element_by_xpath(config.toppage_xpath)
        sleep(1)
        button.click()
        sleep(1)


def get_item(driver):
    """
    コメント、味、サービスのスクレイピング
    """
    assesment_url = driver.current_url
    driver.implicitly_wait(3)
    driver.get(assesment_url)
    assesments = driver.find_elements_by_class_name("des_gdIDUsrImprBox")
    i = 4
    for assesment in assesments:
        if i == 24:
            break
        comment = assesment.find_element_by_xpath(
            f'//*[@id="des_inner"]/div[{i}]/div[3]/table/tbody/tr[3]/td'
        ).text
        comments.append(comment)
        taste = assesment.find_element_by_xpath(
            f'//*[@id="des_inner"]/div[{i}]/div[1]/table/tbody/tr[2]/td[2]/span'
        ).text
        tastes.append(taste)
        service = assesment.find_element_by_xpath(
            f'//*[@id="des_inner"]/div[{i}]/div[1]/table/tbody/tr[3]/td[2]/span'
        ).text
        services.append(service)
        write_csv()
        i += 2
    print(comments, tastes, services)


def write_csv():
    """
    csvに保存
    """
    n = 0
    if n == 0:
        df = pd.DataFrame(
            {"comment": [comments[n]], "taste": [tastes[n]], "service": [services[n]]},
            index=False,
        )
    else:
        append_s = pd.Series([comments[n], tastes[n], services[n],index = ['comment', 'taste', 'service'], name = False])
        df.append(append_s)
        """
        # 行追加で最初に試したコード（動かなかったが一応残す）
        df.append(
            {"comment": [comments[n]], "taste": [tastes[n]], "service": [services[n]]},
            ignore_index=True,
        """
    df.to_csv("assesment.csv")
    n += 1


if __name__ == "__main__":
    driver = main()
    open_target(driver)
    comments = []
    tastes = []
    services = []
    get_item(driver)
