from asyncio import sleep, timeout
from lxml import html
from requests import session
from requests_html import HTML, HTMLSession
import csv

### Local HTML ###
# with open("simple.html") as html_file:
#     source = html_file.read()
#     html = HTML(html=source)

# print(html.html)
# print(html.text)

# match = html.find("title")
# print(match)
# print(type(match))
# print(len(match))
# print(match[0].html)
# print(match[0].text)

# Instead of getting list, we only get the first match
# match = html.find("title", first=True)
# print(match.text)

# match = html.find("#footer", first=True)
# print(match.text)

# article = html.find("div.article", first=True)
# headline = article.find("h2", first=True).text
# summary = article.find("p", first=True).text

# print(headline)
# print(summary)

# articles = html.find("div.article")
# for article in articles:
#     headline = article.find("h2", first=True).text
#     summary = article.find("p", first=True).text
#     print(headline)
#     print(summary)

### Single article from a wordpress website ###
# session = HTMLSession()
# r = session.get("https://www.wpbeginner.com/category/beginners-guide/")
# html = r.html
# print(r.status_code)
# print(r.html)
# article = html.find("article", first=True)
# print(article)
# print(article.text)
# headline = article.find(".entry-title-link", first=True)
# print("Title:", headline.text)
# summary = article.find(".entry-summary p", first=True)
# print("Summary:", summary.text)
# alt_image = article.find(".entry-summary img", first=True)
# return dictionary of attributes
# print(alt_image.attrs)
# print(alt_image.attrs["data-src"])
# alt_image_url = alt_image.attrs["data-src"]
# print(alt_image_url.split("/")[-1])
# link = summary.find("strong", first=True)
# print(link.links)


### multiple article from a wordpress website ###
# with open("wpbeginner_scrape.csv", "w") as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(["headline", "summary"])
#
#     session = HTMLSession()
#     r = session.get("https://www.wpbeginner.com/category/beginners-guide/")
#     html = r.html
#     articles = html.find(
#         "article",
#     )
#     for article in articles:
#         try:
#             headline = article.find(".entry-title-link", first=True)
#         except:
#             headline = None
#         try:
#             summary = article.find(".entry-summary p", first=True)
#         except:
#             summary = None
#
#         print("Title:", headline.text)
#         print("Summary:", summary.text)
#         print()
#
#         csv_writer.writerow([headline.text, summary.text])
# csv_file.close()

### youtube link parsing ###
# test_url = (
#     "https://www.youtube.com/embed/a6fIbtFB46g?si=-xig6KmJ-2ct_bsi&amp;start=1943"
# )
# print(test_url.split("/"))
# base = test_url.split("/")
# core = test_url.split("/")[-1].split("?")[0]
# complete = base[0] + "//" + base[2] + "/watch?v=" + core
# yt_link = f"https://youtube.come/watch?v={core}"
# print(complete)
# print(yt_link)

### Grab links ###
# session = HTMLSession()
# r = session.get(
#     "https://jobvision.ir/jobs/category/data-science-in-tehran?page=1&sort=0"
# )
# links = r.html.links
# for link in links:
#     print(link)

# If you have relative links
# links = r.html.absolute_links
# for link in links:
#     print(link)

### Dynamic Data ###
# with open("simple.html") as html_file:
#     source = html_file.read()
#     html = HTML(html=source)
#     print(type(html))
#     html.render()

# match = html.find("#footer", first=True)
# print(match.html)

# this will not work
# session = HTMLSession()
# r = session.get(
#     "https://jobvision.ir/jobs/category/data-science-in-tehran?page=1&sort=0"
# )
# print(type(r))
# html = r.html.render(sleep=3, timeout=30, keep_page=True, reload=False, scrolldown=1)
# print(html)

### Synchronous task ###
# import time

# session = HTMLSession()
# t1 = time.perf_counter()

# r = session.get("https://httpbin.org/delay/1")
# response = r.html.url
# print(response)

# r = session.get("https://httpbin.org/delay/2")
# response = r.html.url
# print(response)

# r = session.get("https://httpbin.org/delay/3")
# response = r.html.url
# print(response)

# t2 = time.perf_counter()

# print(f"Synchronous: {t2 - t1} seconds")


### Asynchronous ###
# from requests_html import AsyncHTMLSession

# assession = AsyncHTMLSession()


# async def get_delay1():
#     r = await assession.get("https://httpbin.org/delay/1")
#     return r


# async def get_delay2():
#     r = await assession.get("https://httpbin.org/delay/2")
#     return r


# async def get_delay3():
#     r = await assession.get("https://httpbin.org/delay/3")
#     return r


# t1 = time.perf_counter()
# results = assession.run(get_delay1, get_delay2, get_delay3)

# for result in results:
#     response = result.html.url
#     print(response)

# t2 = time.perf_counter()

# print(f"Asynchronous: {t2 - t1} seconds")
