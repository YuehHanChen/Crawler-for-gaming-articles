import requests
import time
from bs4 import BeautifulSoup
import re
from merge import days


def validate_url(url):
    resp = requests.get(url)
    if resp.status_code != 200:  # 若狀態不等於200表示不正常
        return None
    else:
        return resp.text


def validate_article_date(dom,date_list):

    soup = BeautifulSoup(dom,'html5lib')
    all_articles = soup.find_all("article")
    articles_dict = {}
    for article in all_articles:
        for date in date_list:

            if article.find("a",{'href': re.compile('20[0-9]*/'+date)}):
                articles_dict[article.h3.text.strip()] = article.a["href"]
    return articles_dict

#func1 判斷月份天數func：是奇數還偶數月，可以判斷本月天數 ok
#func2 做出找出上個月的func ok
#先找到今天的日期 如果-7之後小於0天，那麼就要用到找上個月的func
#把過去第7天的日期+=1 一直加到今天 到一個串列中
#如果過程中有跨月份，那麼要記得在迴圈中判斷是否到達上個月日期的天數

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

    game = "/?s=game%2C+gaming&sort=date"
    esport = "/?s=esport&sort=date"

    url = "https://a16z.com" + game
    if validate_url(url):
        dom = validate_url(url)
        date_list = give_me_last_several_day_list(days())
        game_articles = validate_article_date(dom, date_list)
        print("A16Z:")
        for i in game_articles.items():
            print(i)

    url = "https://a16z.com" + esport
    if validate_url(url):
        dom = validate_url(url)
        date_list = give_me_last_several_day_list(days())
        esport_articles = validate_article_date(dom, date_list)
        for i in esport_articles:
            if i in game_articles:
                del esport_articles[i]
        if esport_articles:
            for i in esport_articles.items():
                print(i)
