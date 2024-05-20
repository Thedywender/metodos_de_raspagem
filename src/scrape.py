import requests
from bs4 import BeautifulSoup
import re


def scrape(url: str):
    url_base = url.rsplit("/", 2)[0] + "/"
    page = requests.get(url)
    html_content = page.text

    soup = BeautifulSoup(html_content, "html.parser")

    title = soup.select_one("div.product_main > h1").text
    price = re.sub(r"[^\d.]", "", soup.select_one("p.price_color").text)
    description = soup.select_one("#product_description ~ p").text
    suffix = "...more"
    if description.endswith(suffix):
        description = description[: -len(suffix)]
    cover = url_base + soup.select_one("#product_gallery img")["src"]

    return title, price, description, cover


url = (
    "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
)
print(scrape(url))


# _______________________________________________________________________________________
# usando o parsel como metodo de raspagem

# import requests
# import parsel


# def scrape(url: str) -> str:
#     url_prefix = url.rsplit("/", 2)[0] + "/"
#     response = requests.get(url)
#     selector = parsel.Selector(response.text)

#     title = selector.css("h1::text").get()
#     price = selector.css(".product_main > .price_color::text").re_first(
#         r"\d*\.\d{2}"
#     )

#     description = selector.css("#product_description ~ p::text").get()
#     suffix = "...more"
#     if description.endswith(suffix):
#         description = description[: -len(suffix)]

#     cover = url_prefix +
# selector.css("#product_gallery img::attr(src)").get()

#     return f"{title},{price},{description},{cover}"


# print(
#     scrape(
#         "http://books.toscrape.com/catalogue/the-grand-design_405/index.html"
#     )
# )
