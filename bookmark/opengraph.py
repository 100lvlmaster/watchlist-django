from bs4 import BeautifulSoup
import requests

from bookmark.serializer import CreateBookmarkSerliazer


def get_opengraph(url: str):
    page = get_page(url)
    og = parse_og(page)
    og["url"] = url
    return og


def get_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser", from_encoding=response.encoding)
    return soup


def parse_og(soup):
    tags = ("title", "description", "image", "type", "locale")
    ogMap = {}
    for tag in tags:
        ogMap[tag] = get_og_tag(soup, tag)
    return ogMap


def get_og_tag(soup, key):
    content = ""
    if soup.findAll("meta", property=f"og:{key}"):
        content = soup.find("meta", property=f"og:{key}")["content"]
    return content or ""
