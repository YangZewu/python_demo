# Scrapy settings for scrapy_redis_demo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_redis_demo'
LOG_LEVEL = 'ERROR'
SPIDER_MODULES = ['scrapy_redis_demo.spiders']
NEWSPIDER_MODULE = 'scrapy_redis_demo.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.41'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'referer': 'https://book.jd.com/',
    'cookie': '__jdu=16431124550091173755267; shshshfpb=gQouUbz9VH6xnymI503xuUQ; shshshfpa=5069fe1c-6198-6fbc-708e-a3b15bf10e1f-1643205709; unpl=JF8EAKBnNSttWUlSDB4KExAWHlkAW1tYT0RTam5QAwoKQl1QEwoTFUd7XlVdXhRKEB9ubhRUXFNOVA4eAysSEXtdU11UC3sVA2hiDFJfXXtkBhsyGiIQTFhRXV4PSxcCb2INVFpaQ10GHQAZESB7XVxabTh7EAZoYQxdWFx7VTUaMlB8EQZdU1tYC0gQA29mBVFVWExWDRIBHRASSG1WXl0NSCcA; __jdv=122270672|c.duomai.com|t_16282_31648734|tuiguang|037849937d5e47a5ba48dffc88d9996f|1654656101416; joyya=1654656101.1654656122.15.0w2zeqb; areaId=16; shshshfp=c116788d961dd850ec6f0b032936cdda; ipLoc-djd=16-1341-1351-44801; __jda=122270672.16442261101491639827332.1644226110.1655017183.1655389500.58; __jdc=122270672; __jdb=122270672.3.16442261101491639827332|58.1655389500',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'scrapy_redis_demo.middlewares.ScrapyRedisDemoSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'scrapy_redis_demo.middlewares.ScrapyRedisDemoDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#     'scrapy_redis_demo.pipelines.ScrapyRedisDemoPipeline': 300,
#     'scrapy_redis.pipelines.RedisPipeline': 400,
#
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
ITEM_PIPELINES = {
    'scrapy_redis_demo.pipelines.ScrapyRedisDemoPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}
# -- 指定可共享的调度器
# 增加一个去重容器类的配置，使用Redis的set集合来存储请求的指纹数据，从而实现请求去重的持久化存储
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用scrapy_redis组件自己的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 配置调度器是否持久化，再爬虫结束后，是否清空Redis中请求队列和去重指纹的set
SCHEDULER_PERSIST = True
LOG_FILE = "./log.log"
REDIS_HOST = "116.62.194.29"
REDIS_POST = 6379
