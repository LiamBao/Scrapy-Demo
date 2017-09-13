# -*- coding:  utf-8 -*-

# Scrapy settings for lianjiaData_solution project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation: 
#
#     http: //doc.scrapy.org/en/latest/topics/settings.html
#     http: //scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http: //scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'lianjiaData_solution'

SPIDER_MODULES = ['lianjiaData_solution.spiders']
NEWSPIDER_MODULE = 'lianjiaData_solution.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lianjiaData_solution (+http: //www.yourdomain.com)'
USER_AGENT ="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) " \
            "AppleWebKit/537.36 (KHTML, like Gecko)" \
            " Chrome/61.0.3163.79 Safari/537.36"

PAGE_HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"en-US,zh-CN;q=0.8,zh;q=0.6,en;q=0.4",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Host":"sh.lianjia.com",
    "Upgrade-Insecure-Requests":"1",
    "Cookie":"lianjia_uuid=ac820278-08e7-4742-b66d-fa162abfdcb7; UM_distinctid=15e6eecd38b5f6-028c456f557c43-1a376c55-13c680-15e6eecd38c4a6; _smt_uid=59b5ff2e.54d802fc; _jzqa=1.3977188140000239600.1505099569.1505099569.1505099569.1; _jzqc=1; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1505099567; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1505099621; aliyungf_tc=AQAAAMLvgjAb7QsAKXxoQBwDjKvulCP+; select_city=310000; cityCode=sh; gr_user_id=7d38e4b4-9841-4fce-bbf3-36dc1403d6f9; houseThumbType=lshow; ubta=2299869246.3155926997.1505099635716.1505285920062.1505286436461.43; ubtb=2299869246.3155926997.1505286436466.BEBC0B991E28E609D5830C22653F683C; ubtc=2299869246.3155926997.1505286436466.BEBC0B991E28E609D5830C22653F683C; ubtd=43; _gat=1; _ga=GA1.2.1289311238.1505099573; _gat_u=1; gr_session_id_970bc0baee7301fa=8378a532-c318-4178-b3bb-a406743b6360; ubt_load_interval_b=1505287115443; ubt_load_interval_c=1505287115443; __xsptplus696=696.6.1505285416.1505287115.7%234%7C%7C%7C%7C%7C%23%23e1gNuOWxXVQ-JPCStsCe7rDYLQmWR7fx%23; lianjia_ssid=aa4c3048-785d-d8b0-7345-c26f5af424e6",
    "User-Agent": USER_AGENT,
    "Upgrade-Insecure-Requests:1": ""
}


THREAD_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,zh-CN;q=0.8,zh;q=0.6,en;q=0.4",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "sh.lianjia.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": USER_AGENT
}

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default:  16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default:  0)
# See http: //scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of: 
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers: 
#DEFAULT_REQUEST_HEADERS = {
#   'Accept':  'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language':  'en',
#}

# Enable or disable spider middlewares
# See http: //scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'lianjiaData_solution.middlewares.LianjiadataSolutionSpiderMiddleware':  543,
#}

# Enable or disable downloader middlewares
# See http: //scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'lianjiaData_solution.middlewares.MyCustomDownloaderMiddleware':  543,
#}

# Enable or disable extensions
# See http: //scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole':  None,
#}

# Configure item pipelines
# See http: //scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'lianjiaData_solution.pipelines.LianjiadataSolutionPipeline':  500,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http: //doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received: 
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http: //scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# 广度优先
# DEPTH_PRIORITY = 1
# SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
# SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'

import os
# 项目路径
# PROJECT_DIR = os.path.dirname(os.path.abspath(os.path.curdir))



CONCURRENT_REQUESTS=1
CONCURRENT_REQUESTS_PER_DOMAIN=1

HTTPCACHE_ENABLED = True
FEED_EXPORT_ENCODING = 'utf-8'