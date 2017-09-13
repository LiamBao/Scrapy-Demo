#-*- coding=utf8 -*-
# the spider to crawl lianjia.com 
# all rights reserver to Liam Bao (liam_bao@163.com) 

import os
import time
from scrapy import log
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request

from lianjiaData_solution import settings
from lianjiaData_solution.items import LianjiadataSolutionItem


class LianjiaSpider(CrawlSpider):
    name = "lianjia"
    allowed_domains = ["sh.lianjia.com"]
    # allowed_domains = ["https://www.sh.lianjia.com"]
    start_url = "https://sh.lianjia.com/zufang"

    def start_requests(self):
        return [Request(self.start_url,
                        method='GET',
                        headers=settings.PAGE_HEADERS,
                        meta={'cookiejar': 1, 'handle_httpstatus_list': [301, 302]},
                        callback=self.parse_single_page,
                        errback=self.parse_err
                        )]

    def parse_single_page(self, response):
        countNum=100

        for page_num in range(countNum):
            page_url='http://sh.lianjia.com/zufang/d{}'.format(str(page_num+1))
            yield Request(page_url,
                    method='GET',
                    headers=settings.PAGE_HEADERS,
                    meta={'handle_httpstatus_list': [301, 302]},
                    callback=self.thread_url,
                    errback=self.parse_err
                    )

    def thread_url(self, response):
        selector = Selector(response)
        thread=selector.xpath(
                '//ul[@class="house-lst js_fang_list"]/li'
            )
        if thread:
                for single_thread in thread:
                    # aselector = Selector(single_thread)
                    single_url=single_thread.xpath(
                        './/a[@class="js_triggerGray js_fanglist_title"]/@href').extract_first()

                    fang_subway_ex=single_thread.xpath(
                        './/span[@class="fang-subway-ex"]//text()').extract_first()

                    result_kanfang=single_thread.xpath(
                        './/div[@class="square"]/div/span[@class="num"]//text()').extract_first()

                    single_url="{}{}".format(self.start_url.replace('/zufang', ''), single_url)
                    yield Request(single_url,
                            method='GET',
                            meta={
                                    "fang_subway_ex":fang_subway_ex,
                                    "result_kanfang":result_kanfang,
                                    },
                            headers=settings.THREAD_HEADERS,
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
        # a =selector.xpath('.').extract_first().replace('\t', '')
        title=selector.xpath(
            './/div[@class="title"]/h1/text()'
        ).extract_first()

        address=selector.xpath(
            './/p[@class="addrEllipsis"]//text()'
        ).extract_first()

        location=selector.xpath(
            '//table[@class="aroundInfo"]/tr[2]/td[2]//text()'
        ).extract_first()

        #小区 avenue
        avenue=selector.xpath(
            './/p[@class="addrEllipsis"]/@title'
        ).extract_first()

        rent=selector.xpath(
            './/div[@class="price"]/div[1]//text()'
        ).extract_first()
        rent=int(rent.replace('元/月', ''))

        floor=selector.xpath(
            './/table[@class="aroundInfo"]/tr[1]/td[2]//text()'
        ).extract_first()
        floor=floor.replace("楼层：", "")
        #朝向
        house_orientation= selector.xpath(
            './/table[@class="aroundInfo"]/tr[1]/td[4]//text()'
        ).extract_first().strip()

        area=selector.xpath(
            './/div[@class="area"]/div//text()'
        ).extract_first().replace("平", "")

        housing_units="".join(list(selector.xpath(
            './/div[@class="room"]/div//text()'
        ).extract()))

        info=""

        result_kanfang=response.meta['result_kanfang']

        added_time=selector.xpath(
            './/table[@class="aroundInfo"]/tr[2]/td[4]//text()'
        ).extract_first()

        fang_subway_ex=response.meta['fang_subway_ex']

        img_url=selector.xpath(
            './/div[@class="pic-panel pic-panel-hover"]/a/img/@src'
        ).extract_first()

        crawl_time = time.time()

        item = LianjiadataSolutionItem(
            title=title,
            address=address,
            location=location,
            avenue=avenue,
            rent=rent,
            floor=floor,
            house_orientation=house_orientation,
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
