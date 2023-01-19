from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    # https://www.mongodb.com/docs/manual/reference/operator/query/regex/
    try:
        news = search_news({"title": {"$regex": title, "$options": "i"}})
        info = []

        for item in news:
            info.append((item["title"], item["url"]))

        return info

    except news is None:
        return []


# Requisito 7
def search_by_date(date):
    # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    try:
        date_format = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        news = search_news({"timestamp": {"$eq": date_format}})
        info = []

        for item in news:
            info.append((item["title"], item["url"]))

        return info

    except ValueError:
        raise ValueError('Data inválida')


# Requisito 8
def search_by_tag(tag):
    try:
        news = search_news({"tags": {"$regex": tag, "$options": "i"}})
        info = []

        for item in news:
            info.append((item["title"], item["url"]))

        return info

    except news is None:
        return []


# Requisito 9
def search_by_category(category):
    try:
        news = search_news({"category": {"$regex": category, "$options": "i"}})
        info = []

        for item in news:
            info.append((item["title"], item["url"]))

        return info

    except news is None:
        return []
