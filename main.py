from scraper import scrape_books
from cleaner import clean_data
from exporter import export_to_csv

def main():
    print("[*] Scraping data...")
    raw_data = scrape_books(pages=3)

    print("[*] Cleaning data...")
    cleaned_data = clean_data(raw_data)

    print("[*] Exporting data...")
    export_to_csv(cleaned_data)

    print("[✓] Done!")

if __name__ == "__main__":
    main()