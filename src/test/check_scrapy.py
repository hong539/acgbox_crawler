import scrapy

class MySpider(scrapy.Spider):
    name = "myspider"
    start_urls = ["https://example.com"]

    def parse(self, response):
        # Extract title of current page
        title = response.css('title::text').extract_first()
        print(title)

        # Follow links to other pages
        for link in response.css('a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(link), callback=self.parse)