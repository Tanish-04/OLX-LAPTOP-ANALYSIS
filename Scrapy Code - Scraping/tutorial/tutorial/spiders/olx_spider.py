import scrapy
from ..items import TutorialItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class OlxSpider(scrapy.Spider):
    name = 'olx'
    start_urls = [
        'https://www.olx.com.pk/karachi_g4060695/q-laptop'
        #'fhttps://www.olx.com.pk/karachi_g4060695/q-laptop?page={i}' for i in range(1,324)
    ]
    # rules = (
    #     Rule(LinkExtractor(allow=(), restrict_access=('.pageNextPrev',)),
    #          callback="parse",
    #          follow=False),
    # )

    def parse(self, response):
        items = TutorialItem()

        #whole_div = response.css('div.a52608cc _9b1137e6')

        title = response.css("div.a5112ca8::text").extract()
        for i in title:
            print(i)
        price = response.css("div._52497c97 span::text").extract()
        location = response.css("span._424bf2a8::text").extract()
        print(len(title) , len(price) , len(location))
        count = 0
        if len(title) == len(price) == len(location):
            for i in range(len(title)):
                items['title'] = title[i]
                items['price'] = price[i]
                items['location'] = location[i]
                yield items
            else:
                count += 1
        print(count)
        load_more = response.css("a._95dae89d::attr(href)").get()
        if load_more is not None:
            yield response.follow(load_more, callback=self.parse)
        # {
        #     'title': title,
        #     'price': price,
        #     'location': location
        # }
