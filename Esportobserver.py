import time
from bs4 import BeautifulSoup
from Strong import request
from merge import days



def validate_url(url):
    resp = request.get(url,3)
    if resp.status_code != 200:  # 若狀態不等於200表示不正常
        return None
    else:
        return resp.text


def validate_article_date(dom,date_list):

    soup = BeautifulSoup(dom,'html5lib')
    all_articles = soup.find_all("article")
    articles_list = {}

    for article in all_articles:
        if article.find("div", "jeg_meta_date"):
            for date in date_list:
                if article.find("div","jeg_meta_date").text.strip()  == date + ", 2020":
                    articles_list[article.find("h3","jeg_post_title").text.strip()]=article.a["href"]
    return articles_list

def give_me_last_several_day_list(days):
    today = time.strftime("%m/%d").lstrip('0')
    date_list_past_7days = []
    #if today.replace("/", "")[2:4].startswith("0"):
    if today.split("/")[1].startswith("0"):

        if int(today.split("/")[1]) - days <= 0:

            highest_day = odd_or_even(find_last_month())

            seven_days_before = highest_day + int(today.split("/")[1]) - days
            current_month = find_last_month()

            for i in range(days):
                if current_month == find_last_month():

                    if seven_days_before >= 10:
                        date_list_past_7days.append(find_last_month() + " " + str(seven_days_before))
                        seven_days_before += 1
                    else:
                        date_list_past_7days.append(find_last_month() + " " + str(seven_days_before))
                        seven_days_before += 1

                    if seven_days_before > highest_day:
                        current_month = today.split("/")[0]
                        seven_days_before = 1
                else:
                    current_month = Month_dict[int(today.split("/")[0])]
                    date_list_past_7days.append(current_month + " " + str(seven_days_before))
                    seven_days_before += 1

        else:
            seven_days_before = int(today.split("/")[1]) - days
            for i in range(days):
                current_month = Month_dict[int(today.split("/")[0])]
                date_list_past_7days.append(current_month + " " + str(seven_days_before))
                seven_days_before += 1
    else:
        seven_days_before = int(today.split("/")[1]) - days
        for i in range(days):
            current_month = Month_dict[int(today.split("/")[0])]
            if seven_days_before >= 10:
                date_list_past_7days.append(current_month + " " + str(seven_days_before))
                seven_days_before += 1
            else:
                date_list_past_7days.append(current_month + " " + str(seven_days_before))
                seven_days_before += 1



    return date_list_past_7days


def find_last_month():
    today = time.strftime("%m/%d").lstrip('0')
    this_month = today.split("/")[0]
    last_month = ""
    if int(this_month) - 1 <= 0:
        last_month = 12
    else:
        last_month = int(this_month) - 1
    str_month = Month_dict[last_month]
    return str_month


def odd_or_even(month):
    highest_day = 0
    odd_month = ["January", "March", "May", "July", "September", "November"]
    if month in odd_month:
        highest_day = 30
    elif month == "02":
        highest_day = 28
    else:
        highest_day = 31
    return highest_day


if __name__ == '__main__':

    url = "https://esportsobserver.com/"
    Month_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October",
                  11: "November", 12: "December"}
    dom = validate_url(url)
    date_list = give_me_last_several_day_list(days())

    game_articles = validate_article_date(dom, date_list)
    print("Esportobserver:")
    for a in game_articles.items():
        print(a)