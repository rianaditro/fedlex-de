from scrape.scraping import WebScraper


def main():
    scraper = WebScraper('https://www.fedlex.admin.ch/de/cc/internal-law/1')
    scraper.scrape(max_main_buttons=3)

if __name__ == '__main__':
    main()
    