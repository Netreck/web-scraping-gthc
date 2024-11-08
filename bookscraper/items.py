# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# items.py

import scrapy

class BookItem(scrapy.Item):
   url = scrapy.Field()
   title = scrapy.Field()
   upc = scrapy.Field()
   product_type = scrapy.Field()
   price_excl_tax = scrapy.Field()
   price_incl_tax = scrapy.Field()
   tax = scrapy.Field()
   availability = scrapy.Field()
   num_reviews = scrapy.Field()
   stars = scrapy.Field()
   category = scrapy.Field()
   description = scrapy.Field()
   price = scrapy.Field()

class PDF_Item(scrapy.Item):
   url= scrapy.Field()
   paragraph = scrapy.Field()


