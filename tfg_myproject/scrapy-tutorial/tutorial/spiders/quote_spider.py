from pathlib import Path

import scrapy
from bs4 import BeautifulSoup as bs


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    async def start(self):
        urls = [
            "https://thestorygraph.com/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

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