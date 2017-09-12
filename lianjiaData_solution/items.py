# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiadataSolutionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    """
    定义字段属性参数
    """ 
    title=Item.Field()
    address=Item.Field()
    location=Item.Field()
    avenue=Item.Field()
    rent=Item.Field()
    floor=Item.Field()
    area=Item.Field()
    housing_units=Item.Field()
    info=Item.Field()
    result_kanfang=Item.Field()
    added_time=Item.Field()
    fang_subway_ex=Item.Field()
    img_url=Item.Field()
    crawl_time=Item.Field()
