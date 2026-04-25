import requests
from bs4 import BeautifulSoup

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

def scrape_books(pages=2):
    books = []

    for page in range(1, pages + 1):
        url = BASE_URL.format(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        items = soup.select("article.product_pod")

        for item in items:
            title = item.h3.a["title"]
            price = item.select_one(".price_color").text
            rating = item.p["class"][1]  # star-rating

            books.append({
                "title": title,
                "price": price,
                "rating": rating
            })

    return books