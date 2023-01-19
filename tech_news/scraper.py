import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
def scrape_news(html_content: str) -> dict:
    # https://www.w3schools.com/python/ref_string_join.asp
    # https://www.w3schools.com/python/ref_string_strip.asp
    # https://www.w3schools.com/cssref/sel_first-of-type.php
    try:
        selector = Selector(html_content)

        comments_number = selector.css(
                "div.pk-share-buttons-count::text").get()
        string = ""

        info_news = {
            "url": selector.css("link[rel=canonical]::attr(href)").get(),
            "title": selector.css("h1.entry-title::text").get().strip(),
            "timestamp": selector.css("li.meta-date::text").get(),
            "writer": selector.css("a.url.fn.n::text").get(),
            "comments_count": comments_number if comments_number else 0,
            "summary": string.join(selector.css(
                    "div.entry-content > p:first-of-type *::text").getall()
                    ).strip(),
            "tags": selector.css("section.post-tags ul li a::text").getall(),
            "category": selector.css(
                "a.category-style span.label::text").get(),
        }

        return info_news
    except info_news is None:
        return None


# Requisito 5
def get_tech_news(amount):
    # https://developers.google.com/edu/python/lists
    base_url = "https://blog.betrybe.com"
    data_db_latest_news = []
    content = fetch(base_url)
    next_page_url = scrape_next_page_link(content)
    url_news = scrape_updates(content)

    try:
        while len(url_news) < amount:
            next_content = fetch(next_page_url)
            next_page_url = scrape_next_page_link(next_content)
            next_page_news = scrape_updates(next_content)
            url_news.extend(next_page_news)

        for new_base_url in url_news[0:amount]:
            new_content = fetch(new_base_url)
            new_news = scrape_news(new_content)
            data_db_latest_news.append(new_news)

        create_news(data_db_latest_news)

        return data_db_latest_news
    except data_db_latest_news is None:
        return None
