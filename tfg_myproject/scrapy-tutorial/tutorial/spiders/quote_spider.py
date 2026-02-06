from pathlib import Path

import scrapy
from bs4 import BeautifulSoup as bs


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"

    headers={"authority": "www.google.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "referer": "www.google.com",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",}

    async def start(self):
        urls = [
            "https://thestorygraph.com/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        # self.log(response.url.split("/"))

        page = response.url.split("/")[2]
        filename = f"{page}.html"

        # Path(filename).write_bytes(response.body)
        soup = bs(response.body, 'html.parser')
        # Path(filename).write_bytes(prettyHTML)
        out_file = open(f"./{filename}", "w")
        out_file.write(soup.prettify())
        out_file.close()

        self.log(f"Saved file {filename}")