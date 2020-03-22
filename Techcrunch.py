import time
from bs4 import BeautifulSoup
import re
from merge import days
import requests
from Strong import request
from selenium import webdriver
from selenium.common.exceptions import TimeoutException


def validate_url(url):
    resp = request.get(url,3)
    if resp.status_code != 200:  # 若狀態不等於200表示不正常
        if url == "https://techcrunch.com"+a:
            return None
        else:
            validate_url("https://techcrunch.com"+url)
    else:
        return resp.text

def validate_tag(article_link):
    if validate_url(article_link):
        dom =validate_url(article_link)
        soup = BeautifulSoup(dom, 'html5lib')
        a = soup.find("article").text.strip().split(" ")
        title = soup.find("h1","article__title").text.strip()
        if "game" in a or "esport" in a:
            return article_link, title


def validate_article_date(date_list):
    articles_list =[]
    soup = BeautifulSoup(driver.page_source, 'html5lib')
    for date in date_list:
        all_articles =soup.find_all("a",{'href': re.compile('20[0-9]*/'+date)})
        for article in all_articles:
            if article["href"] in articles_list:
                pass
            else:
                articles_list.append(article["href"])
    return articles_list


def give_me_last_several_day_list(days):
    today = time.strftime("%m/%d").lstrip('0')
    date_list_past_7days = []

    if today.split("/")[1].startswith("0"):

        if int(today.split("/")[1]) - days <= 0:

            highest_day = odd_or_even(find_last_month())
            seven_days_before = highest_day + int(today.split("/")[1]) - days
            current_month = find_last_month()

            for i in range(days):
                if current_month == find_last_month():
                    date_list_past_7days.append(find_last_month() + "/" + str(seven_days_before))
                    seven_days_before += 1
                    if seven_days_before > highest_day:
                        current_month = today.split("/")[0]
                        seven_days_before = 1
                else:
                    if len(today.split("/")[0]) != 2:
                        this_month = "0"+today.split("/")[0]
                        date_list_past_7days.append(this_month + "/0" + str(seven_days_before))
                        seven_days_before += 1

        else:
            seven_days_before = int(today.split("/")[1]) - days
            for i in range(days):
                if len(today.split("/")[0]) != 2:
                    this_month = "0" + today.split("/")[0]
                    date_list_past_7days.append(this_month + "/0" + str(seven_days_before))
                    seven_days_before += 1

    else:
        seven_days_before = int(today.split("/")[1]) - days
        for i in range(days):
            if seven_days_before >= 10:
                if len(today.split("/")[0]) != 2:
                    this_month = "0" + today.split("/")[0]
                    date_list_past_7days.append(this_month + "/0" + str(seven_days_before))
                    seven_days_before += 1
            else:
                if len(today.split("/")[0]) != 2:
                    this_month = "0" + today.split("/")[0]
                    date_list_past_7days.append(this_month + "/0" + str(seven_days_before))
                    seven_days_before += 1


    return date_list_past_7days



def find_last_month():
    today = time.strftime("%m/%d").lstrip('0')
    this_month = today.split("/")[0]
    last_month = 0
    if int(this_month) - 1 <= 0:
        last_month = "12"
    else:
        last_month = str(int(this_month) - 1)

    if len(last_month) != 2:
        last_month = "0"+last_month
    return last_month


def odd_or_even(month):
    highest_day = 0
    odd_month = ["01", "03", "05", "07", "09", "11"]
    if month in odd_month:
        highest_day = 30
    elif month == "02":
        highest_day = 28
    else:
        highest_day = 31
    return highest_day


if __name__ == '__main__':

    url = "https://techcrunch.com/"

    try:
        # 啟動Webdriver
        driver = webdriver.Chrome(executable_path='chromedriver 3')
        # Webdriver 的執行檔也可以使用 PhantomJS
        # driver = webdriver.PhantomJS('phantomjs.exe')
        driver.maximize_window()  # 打開瀏覽器之後把視窗放最大
        driver.set_page_load_timeout(90)  # 等待時間最多是60秒，讓他去下載網址資訊
        driver.get(url)  # 使用get去前往該網頁

        time.sleep(15)
        ac = driver.find_element_by_class_name('load-more ')
        driver.execute_script("arguments[0].scrollIntoView();", ac)

        element = driver.find_element_by_class_name('load-more ').click()
        time.sleep(15)
        element = driver.find_element_by_class_name('load-more ').click()
        time.sleep(15)
        element = driver.find_element_by_class_name('load-more ').click()
        time.sleep(15)
        element = driver.find_element_by_class_name('load-more ').click()
        time.sleep(15)
        element = driver.find_element_by_class_name('load-more ').click()
        time.sleep(15)
        element = driver.find_element_by_class_name('load-more ').click()
        time.sleep(15)
        element = driver.find_element_by_class_name('load-more ').click()

        date_list = give_me_last_several_day_list(days())
        game_articles = validate_article_date(date_list)
        print("TechCrunch:")
        target_list = {}
        for i in game_articles:
            if validate_tag("https://techcrunch.com"+i):
                url, title =validate_tag("https://techcrunch.com" + i)
                print(title," => ",url)
                target_list[title] = url
        # for i in target_list.items():
        #     print(i)
    except TimeoutException as ex:
        isrunning = 0
        print("Exception has been thrown. " + str(ex))
        driver.close()

    finally:
        driver.quit()