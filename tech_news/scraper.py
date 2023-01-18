import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url: str) -> str:
    try:
        time.sleep(1)

        response = requests.get(
            url,
            timeout=2,
            headers={"user-agent": "Fake user-agent"})

        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_updates(html_content: str) -> list:
    try:
        selector = Selector(html_content)
        url_news = selector.css("a.cs-overlay-link::attr(href)").getall()
        # warning getattr() it will be used in next release
        return url_news
    except url_news == []:
        return []


# Requisito 3
def scrape_next_page_link(html_content: str) -> str:
    try:
        selector = Selector(html_content)
        next_page_btn = selector.css(
            "a.next.page-numbers::attr(href)").get()
        return next_page_btn
    except next_page_btn is None:
        return None


# Requisito 4
def scrape_news(html_content):
    pass


# Requisito 5
def get_tech_news(amount):
    pass
