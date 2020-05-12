# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyLianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class LianJiaZuFangItem(scrapy.Item):
    房源Id = scrapy.Field()
    房屋标题 = scrapy.Field()
    价格 = scrapy.Field()
    价格单位 = scrapy.Field()
    租赁方式 = scrapy.Field()
    房屋类型 = scrapy.Field()
    朝向楼层 = scrapy.Field()
    链接 = scrapy.Field()
    房源维护时间 = scrapy.Field()
