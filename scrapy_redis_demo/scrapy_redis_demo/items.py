# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyRedisDemoItem(scrapy.Item):
    categoryName = scrapy.Field()
    sonCategoryName = scrapy.Field()
    bookName = scrapy.Field()
    price = scrapy.Field()
    press = scrapy.Field()