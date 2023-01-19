from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    # https://www.mongodb.com/docs/manual/reference/operator/query/regex/
    try:
        titles = search_news({"title": {"$regex": title, "$options": "i"}})
        info = []

        for item in titles:
            info.append((item["title"], item["url"]))

        return info

    except titles is None:
        return []


# Requisito 7
def search_by_date(date):
    pass


# Requisito 8
def search_by_tag(tag):
    pass


# Requisito 9
def search_by_category(category):
    pass
