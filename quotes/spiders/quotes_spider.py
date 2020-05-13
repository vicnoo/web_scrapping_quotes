import scrapy
from ..items import QuotesItem

class QuoteSpider(scrapy.Spider) :
    name = 'quotes'

    page_number = 2

    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]
    
    def parse(self, response) :

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

         #next_page = response.css('li.next a::attr(href)').get()
        next_page = 'http://quotes.toscrape.com/page/' + str(QuoteSpider.page_number) + '/'

         # if next_page is not None:
         #     yield response.follow(next_page, callback = self.parse)
        if QuoteSpider.page_number < 11:
            QuoteSpider.page_number +=1
            yield response.follow(next_page, callback = self.parse)
            
            
         #title = response.css('title::text').extract()
         #yield{
         #    'title_text': title
         #}
         # .a-color-base.a-text-normal