import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import datetime

def processing_date(date_string):
    pattern = r'Submitted (\d{1,2} \w+, \d{4})'
    match = re.search(pattern, date_string)
    if match:
        date = datetime.strptime(match.group(1), '%d %B, %Y')
        formatted_date = datetime.strftime(date, '%Y%m%d')
        return formatted_date

def get_html(query, page):
    search_url = f"https://arxiv.org/search/?query={query}&searchtype=all&source=header&size=50&order=submitted_date&start={50*(page-1)}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

query = "chatgpt"
page = 1
articles = []

while True:
    soup = get_html(query=query, page=page)
    results = soup.find_all("li", class_="arxiv-result")
    print(page)
    if not results:
        break
    for article in results:
        title = article.find("p", class_="title is-5 mathjax").text.strip()
        link = article.find("p", class_="list-title is-inline-block").find("a")["href"]
        date = article.find("p", class_="is-size-7").text.strip()
        date = processing_date(date)
        main_category = article.find("span", class_="tag is-small is-link tooltip is-tooltip-top")['data-tooltip']
        sub_category = article.find_all("span", class_="tag is-small is-grey tooltip is-tooltip-top")
        sub_cat = ""
        if len(sub_category):
            for sub in sub_category:
                sub_cat += sub['data-tooltip']
                sub_cat += ";"
            
        articles.append({"Title": title, "Link": link, "Date": date, "Main Category": main_category, "Sub Category": sub_cat})
    page += 1
df = pd.DataFrame(articles)
df.to_excel("articles.xlsx", index=False)
