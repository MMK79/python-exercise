import requests_html
from requests_html import HTMLSession, AsyncHTMLSession


def retreive_images_links():
    """Open images_download_list.txt file
    Return: list of images links url
    """
    with open("images_download_list.txt", "r") as images_link:
        images_link = images_link.read()
        images_links_list = images_link.split("\n")
        last_one = images_links_list.pop()
        return images_links_list


def scrap_image_link():
    """
    input: images links list
    Return: image links
    """
    images_links_list = retreive_images_links()
    for i in images_links_list:
        print(i)
        session = HTMLSession()
        r = session.get(i)
        html = r.html
        print(html)
        # image_link = r.find("main")
        # print(image_link)
        # for i in image_link:
        #     print(i)


scrap_image_link()
