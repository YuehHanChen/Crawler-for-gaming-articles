import time
from bs4 import BeautifulSoup
from Strong import request
from merge import days



def validate_url(url):
    resp = request.get(url,3)
    if resp.status_code != 200:  
        return None
    else:
        return resp.text


def validate_article_date(dom,date_list):

    soup = BeautifulSoup(dom,'html5lib')
    all_articles = soup.find_all("div","article third col-33 col-spacing")
    articles_dict = {}
    for article in all_articles:
        for date in date_list:
            if article.find("span","date").text.strip() == date+" 2020": #("a",{'href': re.compile('20[0-9]*/'+date)})
                articles_dict[article.h3.text] = article.a["href"]
    return articles_dict


def give_me_last_several_day_list(days):
    today = time.strftime("%m/%d").lstrip('0')
    date_list_past_7days = []
    #if today.replace("/", "")[2:4].startswith("0"):
    if today.split("/")[1].startswith("0"):

        if int(today.split("/")[1]) - days <= 0:

            highest_day = odd_or_even(find_last_month())

            seven_days_before = highest_day + int(today.split("/")[1]) - days
            current_month = find_last_month()

            for i in range(days+1):
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
            for i in range(days+1):
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
    odd_month = ["Jan", "Mar", "May", "Jul", "Sep", "Nov"]
    if month in odd_month:
        highest_day = 30
    elif month == "02":
        highest_day = 28
    else:
        highest_day = 31
    return highest_day


if __name__ == '__main__':

    url = "https://newzoo.com/insights/articles/"
    Month_dict = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct",
                  11: "Nov", 12: "Dec"}
    dom = validate_url(url)
    date_list = give_me_last_several_day_list(days())
    game_articles = validate_article_date(dom, date_list)
    print("Newzoo:")
    for i in game_articles.items():
        print(i)


