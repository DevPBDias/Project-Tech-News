import requests
import time
# from parsel import Selector


def fetch(url):
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
def scrape_updates(html_content):
    pass


# Requisito 3
def scrape_next_page_link(html_content):
    pass


# Requisito 4
def scrape_news(html_content):
    pass


# Requisito 5
def get_tech_news(amount):
    pass
