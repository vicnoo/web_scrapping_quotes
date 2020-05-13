#-----------this code should be in quote_spider.py file ---------------------------
import scrapy
from scrapy.http import FormRequest
from ..items import QuotesItem
from scrapy.utils.response import open_in_browser

class QuoteSpider(scrapy.Spider) :
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/login'
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata = {
            'csrf_token' : token
            ,'username' : 'vicnoo@hotmail.com'
            ,'password' : 'test_@passw0rd'
        },callback = self.start_scraping)
    
    def start_scraping(self,response):
        open_in_browser(response)
        items = QuotesItem()

        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tags = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tags'] = tags

            yield items

    
