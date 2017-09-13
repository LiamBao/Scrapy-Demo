# -*- coding: utf8 -*-

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
    title=scrapy.Field()
    address=scrapy.Field()
    location=scrapy.Field()
    avenue=scrapy.Field()
    rent=scrapy.Field()
    floor=scrapy.Field()
    house_orientation=scrapy.Field()
    area=scrapy.Field()
    housing_units=scrapy.Field()
    info=scrapy.Field()
    result_kanfang=scrapy.Field()
    added_time=scrapy.Field()
    fang_subway_ex=scrapy.Field()
    img_url=scrapy.Field()
    crawl_time=scrapy.Field()
