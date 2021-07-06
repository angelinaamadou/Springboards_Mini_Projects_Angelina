import scrapy


class XPathSpider(scrapy.Spider):
    name = "toscrape-xpath"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            yield {
                'text':quote.xpath("//div[@class='quote']/span[@class='text']").extract(),
                'author': quote.xpath("//div[@class='quote']/span[@class='author']").extract(),
                'tags': quote.xpath("//div[@class='quote']/div[@class='tags']").extract()
                }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
