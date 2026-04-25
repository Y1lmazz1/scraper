import re

def clean_price(price):
    # sadece sayı ve nokta bırak
    cleaned = re.sub(r"[^0-9.]", "", price)
    return float(cleaned) if cleaned else 0.0


def clean_data(data):
    cleaned = []

    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    for item in data:
        cleaned.append({
            "title": item["title"],
            "price": clean_price(item["price"]),
            "rating": rating_map.get(item["rating"], 0)
        })

    return cleaned