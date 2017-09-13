# -*- coding=utf8 -*-
from scrapy import cmdline

cmdline.execute("scrapy crawl lianjia -o lianjiaData.csv".split())
