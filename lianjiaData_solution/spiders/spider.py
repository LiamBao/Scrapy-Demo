#-*- coding=utf8 -*-
# the spider to crawl lianjia.com 
# all rights reserver to Liam Bao (liam_bao@163.com) 

import os
import time
from scrapy import log
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector

from lianjiaData_solution import setting

class LianjiaSpider(CrawlSpider):
    name = "lianjia"
    allowed_domains = ["http://sh.lianjia.com"]
    start_url = "http://sh.lianjia.com/zufang/"


    def start_requests(self):
        """
        登陆页面 获取xrsf
        """
        return [Request(start_url,
                        method='GET',
                        headers=setting.PAGE_HEADERS,
                        callback=self.parse_single_page,
                        errback=self.parse_err
                        )]
    

    def parse_single_page(self, response):
        countNum=100

        for page_num in range(countNum):
            page_url='http://sh.lianjia.com/zufang/d{}'.format(str(page_num))
            yield Request(page_url,
                    method='GET',
                    headers=setting.PAGE_HEADERS,
                    callback=self.thread_url,
                    errback=self.parse_err
                    )


    def thread_url(self, response):
        selector = Selector(response)
        thread=selector.xpath(
                '//ul[@class="house-lst js_fang_list"]'
            ).extract()
        
        if thread_url:
                for single_thread in thread:
                    url=selector.xpath(
                        '//a[class="js_triggerGray js_fanglist_title"]/@href').extract_first()
                    fang_subway_ex=selector.xpath(
                        '//span[@class="fang-subway-ex"]/text()').extract_first()
                    result_kanfang=elector.xpath(
                        '//div[@class="square"]/div/span[@class="num"]/text()').extract_first()

                    single_url="{}{}".format(self.allowed_domains[0], url)
                    yield Request(single_url,
                            method='GET',
                            meta={
                                    "fang_subway_ex":fang_subway_ex,
                                    "result_kanfang":result_kanfang:
                                    }
                            headers=setting.THREAD_HEADERS,
                            callback=self.parse_single_thread,
                            errback=self.parse_err
                            )
        else:
            return 


    def parse_single_thread(self, response):
        """
        parse single thread info
        地址、区域、小区、租金、楼层、面积、户型、介绍、看房记录、上架时间、图片链接、各个房间面积、距离地铁站距离、信息采集时间
        """
        selector = Selector(response)
        title=selector.xpath(
            '//div[@class="title"]/text()'
        ).extract_first().strip()

        address=selector.xpath(
            '//p[@class="addrEllipsis"]/text()'
        ).extract_first().strip()

        location=selector.xpath(
            '//table[@class="aroundInfo"]/tbody/td[1]/text()'
        ).extract_first().strip()

        avenue=selector.xpath(
            '//table[@class="aroundInfo"]/tbody/tr[1]/td[3]/text()'
        ).extract_first().strip()

        rent=selector.xpath(
            '//div[@class="mainInfo bold"]/tbody/text()'
        ).extract_first()
        rent=int(rent.replace('元/月', '').strip())

        floor=selector.xpath(
            '//table[@class="aroundInfo"]/tbody/td[0]'
        ).extract_first().strip()
        floor=floor.replace("楼层：", "").strip()

        area=selector.xpath(
            '//div[@class="area"]/tbody/td[1]'
        ).extract_first().replace("平", "").strip()

        housing_units=selector.xpath(
            '//div[@class="room"]/text()'
        ).extract_first().strip()
        
        info=""

        result_kanfang=response.meta['result_kanfang']

        added_time=selector.xpath(
            '//table[@class="aroundInfo"]/tbody/tr[1]/td[3]/text()'
        ).extract_first().strip()

        fang_subway_ex=response.meta['fang_subway_ex']

        img_url=selector.xpath(
            '//div[@class="pic-panel pic-panel-hover"]/a/img/@href'
        ).extract_first().strip()

        crawl_time = time.time()

        item = LianjiaItem(
            title=title,
            address=address,
            location=location,
            avenue=avenue,
            rent=rent,
            floor=floor,
            area=area,
            housing_units=housing_units,
            info=info,
            result_kanfang=result_kanfang,
            added_time=added_time,
            fang_subway_ex=fang_subway_ex,
            img_url=img_url,
            crawl_time=crawl_time
        )
        yield item

    def parse_err(self, response):
        log.ERROR('crawl {} failed'.format(response.url))
