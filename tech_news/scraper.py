import requests
import time


def fetch(url):
    response = requests.get(url)
    time.sleep(1)
    if (response.status_code == 200):
        return response.text
    elif (response.status_code != 200):
        return None
    elif (requests.Timeout >= 3):
        return None


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
