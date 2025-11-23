from bs4 import BeautifulSoup
import requests
import os
from os import listdir


def retreive_images_links():
    """Open images_download_list.txt file
    Return: list of images links url
    """
    file_name = "images_download_list.txt"
    dir_list = listdir()
    if file_name in dir_list:
        with open(file_name, "r") as images_link:
            images_link = images_link.read()
            images_links_list = images_link.split("\n")
            images_links_list.pop()
            return images_links_list
    else:
        raise Exception(
            "Create a images_download_list.txt and put each link in one line"
        )


def batching(image_l=retreive_images_links()):
    batch_45 = []
    # base case
    if len(image_l) <= 45:
        batch_45.append(image_l)
        return batch_45
    # recursive step
    else:
        return batching(image_l[:45]) + batching(image_l[45:])


def get_html(link):
    return requests.get(link).text


async def image_data_extractor(batch):
    for link in batch:
        html = await get_html(link)
        soup = BeautifulSoup(html, "lxml")
        main_tag = soup.find("main")
        image_div = main_tag.find("img")
        image_dic = image_div.attrs
        image_link = image_dic["src"]
        image_id = image_link.split("/")
        image_id = image_id[-1]
        return [image_link, image_id]


def scrap_image_link():
    """
    input: images links list
    Return: image links
    """
    images_link_id_list = []
    batches = batching()
    for batch in batches:
        images_link_id_list.append(image_data_extractor(batch))
    return images_link_id_list


async def get_images(i):
    return requests.get(i).content


def download_images():
    """Download images
    Return:None"""
    images_link_id_list = scrap_image_link()
    download_path = "/Volumes/MASOUD/Gallery/Background/"
    for image_link_id_list in images_link_id_list:
        image_name = image_link_id_list[1]
        file_loc = os.path.join(download_path, image_name)
        with open(file_loc, "wb") as image:
            image.write(requests.get(image_link_id_list[0]).content)


scrap_image_link()
