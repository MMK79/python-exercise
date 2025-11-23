from bs4 import BeautifulSoup
import requests

# with open("simple.html") as html_file:
# lxml is a html parser, you can use like html5lib
# soup = BeautifulSoup(html_file, "lxml")
# prettify() to sort html
# print(soup.prettify())

# only return the first one that it finds -> requests_html.find('div', first=True)
# article = soup.find("div", class_="article")
# print(article)
# return all articles
# articles = soup.find_all("div", class_="article")
# for article in articles:
#     headline = article.h2.a.text
#     print(headline)
#     summary = article.p.text
#     print(summary)
#     print()

source = requests.get("https://www.wpbeginner.com/blog/").text
soup = BeautifulSoup(source, "lxml")

articles = soup.find_all("article")
# print(article.prettify())
for article in articles:
    headline = article.h2.a.text
    print(headline)
    summary = article.find("div", class_="entry-summary").text
    print(summary)
    print()
